---
type: concept
title: "STM32 Digital Control for Buck Converter"
created: 2026-05-05
updated: 2026-05-05
tags:
  - concept
  - domain/engineering
  - power-electronics
  - embedded
  - STM32
  - control-systems
status: complete
complexity: advanced
domain: engineering
aliases: ["STM32 buck control", "digital PWM control STM32", "TIM1 buck converter"]
related:
  - "[[Buck Converter Theory and Design]]"
  - "[[Buck Converter LTspice Simulation]]"
  - "[[Buck Converter PCB Design and Fabrication]]"
  - "[[Signals and Systems — Laplace and Fourier]]"
  - "[[Transfer Functions and Poles Zeros]]"
sources:
  - "[[Research - Buck Converter Build Guide]]"
---
# STM32 Digital Control for Buck Converter

Complete guide to implementing the digital control loop for the 12V→5V, 1A, 100 kHz synchronous buck converter using an STM32 Nucleo board.

## 1. Why STM32 for a Buck Converter

The STM32F446RE (Nucleo-64 board, ~$15) provides:
- **TIM1 and TIM8**: Advanced-control timers with complementary PWM outputs and hardware dead-time insertion — exactly what synchronous buck gate drive requires
- **12-bit ADC** at up to 5.1 MSPS (well above the 100 kHz switching frequency)
- **ADC trigger from timer**: can sample at the exact peak or valley of the PWM carrier, avoiding switching noise — critical for accurate feedback
- **168 MHz clock**: enables 100 kHz PWM with fine duty-cycle resolution (1680 steps = 0.06% resolution)

## 2. Hardware Setup

### STM32 Nucleo-64 Connections

| STM32 Pin | Function | Connects To |
|-----------|----------|-------------|
| PA8 (TIM1_CH1) | High-side PWM | Gate driver HIN input |
| PB13 (TIM1_CH1N) | Low-side PWM (complementary) | Gate driver LIN input |
| PA0 (ADC1_IN0) | Output voltage sense | Feedback voltage divider (Vout/2) |
| GND | Common ground | Gate driver GND + power stage GND |

**Important**: The STM32 operates at 3.3V logic. The IR2110 gate driver accepts 3.3V logic at its HIN/LIN inputs when VDD = 3.3V — confirm this in the datasheet (VDD range: 3V–20V).

### Gate Driver: IR2110

The IR2110 is a half-bridge gate driver IC that:
- Provides 10–12V gate drive (from VCC) to both high-side and low-side MOSFETs
- Handles the floating high-side gate drive via a bootstrap circuit
- Accepts logic-level inputs (3.3V compatible when VDD = 3.3V)

**IR2110 Pin Connections**:

| Pin | Connection | Value |
|-----|-----------|-------|
| VDD | STM32 3.3V | Logic supply |
| VCC | 12V | Gate drive supply |
| VB | VCC via bootstrap diode + capacitor | High-side bootstrap supply |
| VS | Switching node (drain-source junction) | Bootstrap return |
| HO | High-side MOSFET gate | Via 10Ω gate resistor |
| LO | Low-side MOSFET gate | Via 10Ω gate resistor |
| HIN | TIM1_CH1 (PA8) | High-side control input |
| LIN | TIM1_CH1N (PB13) | Low-side control input |
| SD | 3.3V (enable) | Shutdown pin, active LOW |

**Bootstrap Circuit**:
```
VCC (12V) ──── D_boot (UF4007) ──── VB ────┬──── C_boot (220 nF) ──── VS
                                            └──── HO → high-side gate
```
The bootstrap capacitor charges when the low-side MOSFET conducts (VS ≈ GND). When the high-side switches ON, VS rises to ~12V and VB rises to ~24V, providing the gate drive above the switching node.

**Bootstrap capacitor sizing**:
```
C_boot ≥ Qg / ΔV_allowed = 63 nC / 1V ≈ 63 nF → use 220 nF
```

## 3. TIM1 PWM Configuration

### Clock Setup

For 100 kHz PWM from 168 MHz system clock:
```
Timer prescaler: PSC = 0 (no prescaling, timer runs at 168 MHz)
Auto-reload register: ARR = 1679 (edge-aligned up-counting)
→ Period = (ARR+1) / f_clk = 1680 / 168 MHz = 10 µs → f_sw = 100 kHz ✓
```

For center-aligned (preferred for reduced EMI and symmetric current sensing):
```
ARR = 839 (counter counts 0→839→0 = 1680 ticks per cycle)
→ Same 100 kHz switching frequency
→ Sampling at counter peak (839) or valley (0) gives minimum ripple point
```

### Duty Cycle Register

```c
// For D = 41.7% (5V out from 12V in):
// CCR1 = D × (ARR+1) = 0.417 × 1680 ≈ 701
TIM1->CCR1 = 701;
```

In the control loop, this value is updated every switching cycle based on the PI controller output.

### Dead Time Configuration (BDTR Register)

Dead time prevents shoot-through (both MOSFETs conducting simultaneously).

The BDTR register DTG[7:0] field encodes dead time. For 100 ns dead time at 168 MHz:
```
100 ns × 168 MHz = 16.8 ≈ 17 timer ticks
DTG = 17 (binary: 00010001) → dead time ≈ 101 ns
```

This is plenty of margin for the IRLZ44N's rise/fall time (< 30 ns at 10V gate drive with 10Ω Rg).

### STM32CubeIDE Setup (Step-by-Step)

1. **Open STM32CubeIDE** → New STM32 Project → select NUCLEO-F446RE
2. **Pinout & Configuration**:
   - Timers → TIM1 → Mode: PWM Generation CH1, Channel: Channel 1 Complementary
   - Enable TIM1 Global Interrupt
3. **TIM1 Parameter Settings**:
   - Prescaler: 0
   - Counter Mode: Center Aligned mode 1
   - Counter Period (ARR): 839
   - Dead Time: 17
   - Break And Dead-Time Register → enable OSSR and OSSI
4. **PWM Mode**: PWM Mode 1 (output high when counter < CCR1)
5. **ADC1 Configuration**:
   - Mode: IN0 (PA0) single conversion
   - Trigger Source: TIM1 Trigger Out (TRGO) → Counter matches update event
   - Sampling Time: 3 cycles (fast for low-impedance source)
6. **Generate Code** → open main.c

### C Code Implementation

```c
// main.c additions (after generated HAL init code)

#define V_REF_COUNTS   1680   // ADC reading corresponding to 5.0V output
// Vout sensed via 1:2 divider (10kΩ / 10kΩ) → 5V/2 = 2.5V at ADC
// 2.5V / 3.3V × 4096 (12-bit) ≈ 3103 ADC counts for 5.0V Vout
#define V_REF_ADC      3103   

// PI controller parameters (tune these!)
#define KP             0.2f
#define KI             500.0f   // units: per second, integrated each control period (10µs)
#define DT             0.00001f // 10 µs control period
#define MAX_DUTY       800      // maximum CCR1 value (duty cap at 95%)
#define MIN_DUTY       0        // minimum CCR1 value

float integral = 0.0f;

// Called from TIM1 Update Interrupt (every 10µs = 100 kHz)
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim) {
    if (htim->Instance == TIM1) {
        // Read ADC (triggered by TIM1, result ready by now)
        uint32_t adc_val = HAL_ADC_GetValue(&hadc1);
        
        // Compute error (positive = output too low, need more duty cycle)
        float error = (float)(V_REF_ADC - adc_val);
        
        // PI control
        integral += error * DT;
        // Anti-windup: clamp integral
        if (integral > MAX_DUTY / KI) integral = MAX_DUTY / KI;
        if (integral < 0) integral = 0;
        
        float duty_f = KP * error + KI * integral;
        
        // Clamp to valid range
        int32_t duty = (int32_t)duty_f;
        if (duty > MAX_DUTY) duty = MAX_DUTY;
        if (duty < MIN_DUTY) duty = MIN_DUTY;
        
        // Update duty cycle (takes effect next PWM cycle)
        TIM1->CCR1 = (uint32_t)duty;
        
        // Restart ADC for next cycle
        HAL_ADC_Start(&hadc1);
    }
}

// In main(), before the while(1) loop:
// HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);         // Start high-side PWM
// HAL_TIMEx_PWMN_Start(&htim1, TIM_CHANNEL_1);      // Start low-side complementary PWM
// HAL_ADC_Start(&hadc1);                              // Start ADC
// HAL_TIM_Base_Start_IT(&htim1);                      // Enable TIM1 interrupt
```

## 4. Feedback Voltage Divider

The ADC input must stay within 0–3.3V. Vout = 5V → use a 1:2 divider:

```
Vout ──── R1 (10 kΩ) ──── V_sense ──── PA0 (ADC)
                             │
                           R2 (10 kΩ)
                             │
                           GND
```

V_sense = Vout × R2/(R1+R2) = 5V × 0.5 = 2.5V ✓ (well within 3.3V ADC range)

Add a 100 nF ceramic capacitor from V_sense to GND, placed immediately at the ADC pin, to filter switching noise.

**ADC calibration**: The actual Vout = V_sense × 2 × (3.3V / 4096) × adc_reading. Pre-calibrate by measuring actual 3.3V rail with a DMM and adjusting accordingly.

## 5. Tuning the PI Controller

### Step 1: Start Open-Loop

Disable the PI interrupt and manually set CCR1:
```c
TIM1->CCR1 = 701; // D = 41.7% → should give ~5V Vout
```

Measure Vout with a DMM. If it's in the right ballpark (4.5–5.5V), the hardware is working. Adjust CCR1 manually to dial in 5.00V — note this CCR1 value as your starting point.

### Step 2: Close the Loop with Kp Only (Ki = 0)

Start with Kp = 0.05, Ki = 0. Enable the PI interrupt. Check:
- Does Vout stabilize near 5V?
- Is there oscillation? (if yes, reduce Kp by 2×)
- How close to 5V? (steady-state error is expected with P-only control)

### Step 3: Add Integral Term

Slowly increase Ki (e.g., 100, 200, 500) until:
- Steady-state error → 0 (Vout = 5.00V ± 10 mV)
- No oscillation or ringing in Vout

### Step 4: Test Transient Response

Suddenly connect/disconnect a second 10Ω resistor in parallel with the main 5Ω load (load step from 1A to 1.5A and back). Watch on oscilloscope:
- Vout dip: target < 200 mV
- Recovery time: target < 1 ms

If Vout dips too much → increase Kp. If ringing → reduce Kp or Ki.

## 6. Beginner Exercises Before Buck Converter (Weeks 1–3)

Complete these to build STM32 confidence:

### Exercise 1: LED Blink (GPIO)
```c
// Toggle PA5 (onboard LED) every 500ms
HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);
HAL_Delay(500);
```

### Exercise 2: PWM LED Dimming (Timer)
Configure TIM2 for 10 kHz PWM on PA5. Use a for-loop to sweep CCR1 from 0 to ARR, creating a "breathing" LED effect. This teaches you how ARR and CCR relate before connecting to power circuits.

### Exercise 3: ADC Reading
Read PA0 (potentiometer) and print via UART to PC:
```c
HAL_ADC_Start(&hadc1);
HAL_ADC_PollForConversion(&hadc1, 100);
uint32_t val = HAL_ADC_GetValue(&hadc1);
printf("ADC: %lu  Voltage: %.2f V\r\n", val, val * 3.3f / 4096);
```

### Exercise 4: UART-Controlled PWM
Receive a number 0–100 over UART, set PWM duty cycle to that percentage. This validates your PWM control code before live power electronics.

### Exercise 5: Timer Interrupt at 100 kHz
Set up TIM1 interrupt at 100 kHz and toggle a GPIO pin inside it. Verify with oscilloscope that the pin toggles at exactly 50 kHz (toggling every interrupt = 100 kHz/2). This proves your interrupt timing before closing the control loop.

## 7. Safety Checklist Before Powering the Hardware

- [ ] Verify gate signals on oscilloscope BEFORE connecting to power stage (use 5V USB supply only)
- [ ] Confirm dead time is visible on scope between HO and LO transitions
- [ ] Verify VB bootstrap voltage rises (measure VB-VS with isolated probe or DMM during light load)
- [ ] Start at low input voltage: use 5V bench supply first, not 12V
- [ ] Current limit on bench supply to 500 mA initially
- [ ] Have a current-limiting resistor (10Ω, 5W) in series with Vin initially (limits fault current)
- [ ] Check MOSFET temperature after 30 seconds at full load (should be < 60°C at room temperature)

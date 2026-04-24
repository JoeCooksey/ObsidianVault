---
type: concept
title: "C++ in Electrical Engineering"
status: developing
created: 2026-04-24
updated: 2026-04-24
tags:
  - cpp
  - c-language
  - electrical-engineering
  - embedded-systems
  - firmware
  - motor-control
  - power-electronics
  - rtos
---

# C++ in Electrical Engineering

C (and C++) is the **real-time execution layer** of physical EE. Where Python designs, simulates, and automates, C runs inside the hardware — in microcontrollers, DSPs, FPGAs, and motor drives — at speeds too fast for any interpreted language.

**Practical rule**: If something must execute reliably within microseconds, it's written in C. If it's running on a desktop analyzing data from that C system, it's probably Python.

---

## Where C/C++ Lives in Physical EE

### 1. Embedded Microcontroller Firmware
Every MCU (microcontroller unit) is programmed in C or C++. The MCU reads sensors, runs algorithms, and drives actuators. C is preferred over C++ for embedded because:
- Smaller binary footprint (no vtable overhead, no exceptions)
- Deterministic execution (no garbage collector)
- Direct hardware register access via memory-mapped I/O

**Register-level GPIO in C (STM32 example):**
```c
// Turn on LED connected to PA5 (no HAL abstraction)
RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;   // enable GPIOA clock
GPIOA->MODER |= (1 << 10);              // PA5 = output mode
GPIOA->ODR   |= (1 << 5);              // PA5 HIGH = LED on
```

**Common MCU families in EE:**
| Family | Vendor | Typical EE use |
|--------|--------|---------------|
| STM32 | STMicroelectronics | General-purpose embedded, motor control |
| TI C2000 | Texas Instruments | Power electronics DSP (EV, industrial) |
| ESP32 | Espressif | IoT, wireless sensor nodes |
| RP2040 | Raspberry Pi | DIY / prototyping |
| ATmega | Microchip (Arduino) | Learning, low-power |
| dsPIC | Microchip | Motor control, power conversion |

---

### 2. Digital Power Converter Control (TI C2000)
The **TI C2000 F28379D** is the industry-standard DSP for automotive and industrial power electronics. It runs:

- **PI current control loops** at 10–100 kHz update rates
- **SVPWM** (Space Vector PWM) generation for 3-phase inverters
- **Dead time compensation** in SiC/GaN gate drivers
- **Fault detection and protection** (overcurrent, overvoltage, overtemperature)
- **CAN bus communication** to BMS and VCM

This chip is inside commercial EV traction inverters and DCFC chargers. Knowing C2000 + C is a direct hiring signal for SiC/GaN power electronics roles.

**PI loop structure (C, C2000):**
```c
float pi_controller(float setpoint, float measured) {
    static float integral = 0.0f;
    float error = setpoint - measured;
    integral += KI * error * DT;
    integral = CLAMP(integral, -IMAX, IMAX);  // anti-windup
    return KP * error + integral;
}
```

The C2000 runs this inside a PWM interrupt at 100 kHz — 10 microseconds per iteration.

---

### 3. RTOS — Real-Time Operating Systems
A **Real-Time Operating System (RTOS)** is required when a system must do multiple things simultaneously with guaranteed timing:
- Simultaneously measure ADC, run control loop, communicate CAN, update display
- **FreeRTOS** (most common; C; free under MIT license) — runs on STM32, ESP32, C2000
- **Zephyr RTOS** (open source; C; Linux Foundation) — growing in automotive

**Key RTOS concepts in C:**
```c
// Create a task at 10 kHz
xTaskCreate(control_loop_task, "ControlLoop", 256, NULL, HIGH_PRIORITY, NULL);

// A FreeRTOS task
void control_loop_task(void *pvParameters) {
    TickType_t lastWakeTime = xTaskGetTickCount();
    for(;;) {
        run_control_loop();
        vTaskDelayUntil(&lastWakeTime, pdMS_TO_TICKS(0.1)); // 100 µs period
    }
}
```

---

### 4. Communication Protocols
Physical EE systems talk to each other over buses — all implemented in C:

| Protocol | Physical use | C implementation |
|----------|-------------|-----------------|
| **CAN bus** | EV BMS/inverter/charger comms | STM32 bxCAN, MCP2515, AUTOSAR |
| **SPI** | ADC, DAC, display, MOSFET gate driver IC | HAL_SPI_Transmit() |
| **I2C** | Sensors (IMU, temp sensor, EEPROM) | HAL_I2C_Master_Transmit() |
| **UART** | Debug output, GPS, Bluetooth modules | printf() redirected to USART |
| **PWM** | Motor control, DC-DC converter duty cycle | Timer peripheral config |
| **Modbus** | Industrial power electronics, inverters | libmodbus (C library) |

---

### 5. Safety-Critical Firmware — MISRA-C
**MISRA-C** (Motor Industry Software Reliability Association) is the coding standard for automotive and safety-critical embedded systems. Required by:
- **ISO 26262** (automotive functional safety — ASIL A/B/C/D)
- **DO-178C** (avionics software)
- **IEC 61508** (industrial safety)

Key MISRA-C rules:
- No dynamic memory allocation (`malloc`, `free` are banned)
- No recursion
- All variables initialized before use
- No unreachable code
- Single point of exit per function (no multiple returns)

This is why automotive firmware is C, not Python or C++. Knowing MISRA fundamentals is a differentiator for any automotive EE role.

---

### 6. DSP Signal Processing in C — ARM CMSIS-DSP
The **ARM CMSIS-DSP** library is a free, hardware-optimized C library of DSP functions for any ARM Cortex-M MCU:

- FFT (real and complex): `arm_rfft_fast_f32()`
- FIR filter: `arm_fir_f32()`
- IIR biquad filter (BiQuad): `arm_biquad_cascade_df2T_f32()`
- PID controller: `arm_pid_f32()` / `arm_pid_q31()`
- Matrix operations: `arm_mat_mult_f32()`

This is the C equivalent of SciPy's signal library — but running on a 168 MHz Cortex-M4 inside a motor drive.

---

### 7. Motor Control — Field Oriented Control (FOC)
FOC (Field Oriented Control) is the dominant algorithm for BLDC and PMSM motor drives (EV motors, servo drives, industrial robots). It runs in C/C++ on an MCU/DSP:

**FOC pipeline (C):**
1. Read 3-phase motor currents (ADC)
2. Clarke transform: 3-phase → α-β frame (C math)
3. Park transform: α-β → d-q rotating frame (C math, requires sin/cos)
4. PI control of d and q axis currents (C, runs at 10–50 kHz)
5. Inverse Park + Clarke: d-q → 3-phase
6. SVPWM generation → PWM output to inverter gate drivers

STMicroelectronics provides free **ST Motor Control Workbench** with auto-generated C code for STM32-based FOC drives.

---

### 8. C vs. C++ in Embedded EE

| Aspect | C | C++ |
|--------|---|-----|
| Memory | Lower overhead | Higher (vtables, exceptions) |
| Safety standards | Required (MISRA-C) | MISRA-C++ exists but less common |
| Embedded use | 80%+ of embedded firmware | Arduino, HAL layers, some middleware |
| OOP benefits | Structs + function pointers | Full classes, inheritance, templates |
| Recommendation | Learn C first for embedded | Add C++ after C is solid |

**The rule**: Learn C first. Every C++ skill in embedded systems builds on C. MISRA requires C. The TI C2000 Academy uses C. Arduino is C++ but uses C idioms.

---

## The Physical-EE C/C++ Toolchain

```
Source code (.c/.cpp)
    ↓
Compiler (arm-none-eabi-gcc or TI CGT)
    ↓
Object files + linker → ELF binary
    ↓
Debugger (OpenOCD + GDB or J-Link)
    ↓
Flash to MCU via SWD/JTAG
    ↓
Real hardware running
```

**Free tools:**
- **GNU Arm Embedded Toolchain** — free, cross-platform C/C++ compiler for ARM MCUs
- **STM32CubeIDE** — free Eclipse-based IDE from ST; integrated debugger; HAL code gen
- **Code Composer Studio (CCS)** — free TI IDE for C2000
- **VS Code + Cortex-Debug extension** — modern alternative; GDB integration
- **OpenOCD** — open-source JTAG/SWD debug interface

---

## Related
- [[C++ Self-Teaching Roadmap for EE]]
- [[Python in Electrical Engineering]]
- [[EE Physical Side — Actionable Skill Plan]]
- [[Research - Python and C++ in Electrical Engineering]]
- [[EE Freshman Action Plans]]
- [[EE Freshman Self-Study Stack]]

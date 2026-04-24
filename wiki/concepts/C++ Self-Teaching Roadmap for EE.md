---
type: concept
title: "C++ Self-Teaching Roadmap for EE"
status: developing
created: 2026-04-24
updated: 2026-04-24
tags:
  - cpp
  - c-language
  - self-teaching
  - roadmap
  - embedded-systems
  - electrical-engineering
  - firmware
  - rtos
---

# C++ Self-Teaching Roadmap for EE

A phased roadmap for learning C/C++ from scratch through professional embedded EE firmware skills. Total timeline: **12–24 months** of part-time study (~3–5 hrs/wk). Begins at Phase 0 (pure C, no OOP) and progresses to TI C2000 power electronics DSP — the end-state that directly maps to WBG power electronics roles.

**Important**: Learn C before C++. Embedded EE firmware is predominantly C. C++ is used in higher layers (Arduino, HAL wrappers, some RTOS middleware), but the lowest-level hardware code — the code that runs in ISRs and controls power converters — is C.

---

## Phase 0 — C Language Fundamentals (Month 1–2, 4–5 hrs/wk)

**Goal**: Write correct C programs from scratch. Understand pointers. Understand how memory works.

### Why C before C++?
- MISRA-C (automotive safety standard) requires C, not C++
- TI C2000 DSP uses C primarily
- FreeRTOS is pure C
- C forces you to understand what the hardware is actually doing (no hidden allocations, no garbage collector)
- Every C++ skill transfers cleanly to C; the reverse is not always true

### Core C concepts to master

**Pointers — the most important C concept for embedded:**
```c
int x = 42;
int *ptr = &x;         // ptr holds the ADDRESS of x
printf("%d\n", *ptr);  // dereference: prints 42
*ptr = 100;            // changes x through ptr
printf("%d\n", x);     // prints 100

// Memory-mapped hardware register access (the whole point for embedded):
#define GPIOA_ODR  (*((volatile uint32_t*)0x40020014))  // GPIOA output data register
GPIOA_ODR |= (1 << 5);  // set bit 5 = turn on PA5 pin
```

**Structs and bit-fields (represent hardware registers):**
```c
typedef struct {
    uint32_t MODE   : 2;   // 2-bit mode field
    uint32_t OEN    : 1;   // 1-bit output enable
    uint32_t PULLUP : 1;   // 1-bit pullup enable
    uint32_t RESERVED : 28;
} GPIO_PIN_REG;
```

**Other essentials**: arrays, strings, functions, recursion (understand it; avoid in embedded), `#define` macros, `typedef`, `enum`, `union`.

### Resources
1. **"The C Programming Language" (K&R)** — Kernighan & Ritchie, 2nd ed. (~$25 used). The definitive reference. Work through all exercises. Start with Ch. 1–5.
2. **CS50 (cs50.harvard.edu)** — Harvard's free intro CS course uses C. Lectures 1–4 cover C essentials. Free, excellent video lectures.
3. **Learn C (learn-c.org)** — free browser-based interactive exercises. Good for drilling syntax.
4. **cppreference.com** — the authoritative C/C++ reference. Bookmark it.

### Tools (free)
- **GCC on Linux/WSL** or **MinGW** on Windows — compile and run C on desktop
- VS Code + C/C++ extension — syntax highlighting, IntelliSense
- **WSL2 (Windows Subsystem for Linux)** — run a real Linux environment on Windows; most embedded tools work better in Linux

### Milestones
- [ ] Wrote a function that takes a pointer and modifies the pointed-to value
- [ ] Implemented a simple linked list using structs and pointers
- [ ] Understood the difference between `int *p = &x` and `int p = x` — no guessing
- [ ] Wrote a function that reads from a simulated hardware register (uint32_t pointer to a fixed address)
- [ ] Completed at least 2 K&R exercises per chapter

---

## Phase 1 — Arduino C++ (Embedded Basics) (Month 2–4, 3–4 hrs/wk)

**Goal**: Write real embedded firmware. Control real hardware. Bridge circuit theory and software.

This builds directly on [[EE Freshman Action Plans]] Action Plan 6 (Arduino). If you've done that plan, this phase extends it.

### What Arduino actually is
Arduino sketches are C++ compiled with avr-g++ for ATmega MCUs (Uno, Nano) or arm-none-eabi-g++ for ARM-based Arduinos (Mega 2560, Due). The Arduino library wraps low-level register access in readable functions:
```cpp
// Arduino C++ (high-level)
pinMode(13, OUTPUT);      // internally sets DDRB |= (1 << 5)
digitalWrite(13, HIGH);   // internally sets PORTB |= (1 << 5)
analogWrite(9, 128);      // sets up Timer1 PWM at 50% duty cycle
int val = analogRead(A0); // reads 10-bit ADC (0–1023)
```

### Key projects (beyond Action Plan 6)
| Project | Concept demonstrated |
|---------|---------------------|
| Voltage measurement display | ADC → calibration → Serial output |
| RC charging curve logger | ADC sampling over time → math verification |
| PWM signal generator | Timer + duty cycle → oscilloscope verification |
| I2C sensor reading | Wire library → I2C protocol → struct unpacking |
| UART state machine | Receive commands, parse, execute → FSM pattern |
| PID LED brightness control | Feedback control loop in C++ on MCU |

### Bare-metal optional (Extend beyond Arduino)
Once Arduino is comfortable, try programming an ATmega or Arduino **without the Arduino library** — directly write to registers. This teaches how abstractions work.

```c
// Bare metal: blink PA5 on AVR ATmega328
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    DDRB |= (1 << PB5);  // PB5 = Arduino pin 13 = output
    while(1) {
        PORTB ^= (1 << PB5);  // toggle pin
        _delay_ms(500);
    }
}
```

### Milestones
- [ ] PWM output verified on oscilloscope (or with LED fading)
- [ ] ADC reading calibrated to real voltage (calibration factor applied)
- [ ] I2C sensor data parsed correctly into a struct
- [ ] State machine responding correctly to UART commands
- [ ] Simple PID loop implemented (even for LED brightness)

---

## Phase 2 — STM32 with HAL (Professional MCU) (Month 4–7, 3–5 hrs/wk)

**Goal**: Use an industry-grade ARM MCU. Learn the peripheral driver model used in professional firmware.

STM32 (ARM Cortex-M) is the most common MCU family in professional embedded EE. STMicroelectronics provides free tools and a hardware abstraction layer (HAL) that is used in real products.

### Hardware
**STM32 Nucleo-F446RE** (~$15 on Mouser/Digi-Key) — Cortex-M4 at 180 MHz, FPU, all peripherals.

### Tools (all free)
- **STM32CubeIDE** — free Eclipse-based IDE from ST; includes HAL code generator, GDB debugger
- **STM32CubeMX** — graphical pin/peripheral configurator → auto-generates HAL init code
- **ST-Link** — on-board debugger on every Nucleo board

### Peripheral skills to develop (in order)
```
GPIO → UART → Timer → PWM → ADC → SPI → I2C → DMA → Interrupts → CAN
```

**Each peripheral follows the same HAL pattern:**
```c
// UART transmit (HAL)
uint8_t msg[] = "Voltage: 3.30 V\r\n";
HAL_UART_Transmit(&huart2, msg, strlen((char*)msg), HAL_MAX_DELAY);

// ADC single conversion
HAL_ADC_Start(&hadc1);
HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
uint32_t raw = HAL_ADC_GetValue(&hadc1);
float voltage = raw * 3.3f / 4096.0f;  // 12-bit ADC, 3.3 V reference
```

### Key projects at this phase
1. **Voltage logger**: Read ADC, timestamp with SysTick, transmit over UART to PC, plot in Python. This is a complete EE measurement system.
2. **PWM signal generator**: Configure a timer for PWM, control duty cycle via UART command. Verify output on oscilloscope.
3. **SPI DAC output**: Generate a sine wave by writing samples to a DAC over SPI. Verify with oscilloscope.
4. **Interrupt-driven control**: Configure timer interrupt at 10 kHz, run control calculation in ISR.

### Resources
- **STM32CubeIDE documentation + examples** — free from ST
- **"Mastering STM32" by Carmine Noviello** — best STM32 textbook; Leanpub, ~$20
- **"Embedded Systems with ARM Cortex-M Microcontrollers in Assembly Language and C" by Jonathan Valvano** — partially free at utexas.edu/~valvano
- **DigiKey YouTube series** — "Intro to RTOS" and "STM32" tutorials; free, very good

### Milestones
- [ ] STM32 Nucleo blinking LED via HAL GPIO
- [ ] UART transmitting to serial terminal
- [ ] ADC reading verified against real multimeter measurement
- [ ] Timer PWM output verified on oscilloscope
- [ ] Interrupt triggering at correct rate (verify with oscilloscope or logic analyzer)

---

## Phase 3 — FreeRTOS (Real-Time Operating System) (Month 7–10, 3 hrs/wk)

**Goal**: Write multi-tasking firmware with guaranteed timing. This is what runs inside commercial power electronics.

### Why RTOS in EE
A standalone `while(1)` loop can only do one thing at a time. An RTOS lets you:
- Run a 10 kHz control loop as a high-priority task
- Simultaneously handle CAN bus messages at medium priority
- Log data to SD card at low priority
- All preemptively scheduled — none of them block each other

### FreeRTOS fundamentals in C

**Tasks (the basic unit of FreeRTOS)**:
```c
void control_task(void *pvParameters) {
    TickType_t lastWakeTime = xTaskGetTickCount();
    for(;;) {
        // Run control algorithm
        float setpoint = 5.0f;
        float measured = read_adc_voltage();
        float output = pi_controller(setpoint, measured);
        set_pwm_duty(output);
        
        // Wait until exactly 100 µs has elapsed since lastWakeTime
        vTaskDelayUntil(&lastWakeTime, pdUS_TO_TICKS(100));
    }
}

// Create the task at priority 5 (higher = higher priority)
xTaskCreate(control_task, "Control", 512, NULL, 5, NULL);
vTaskStartScheduler();
```

**Queues (inter-task communication — thread-safe)**:
```c
QueueHandle_t xDataQueue = xQueueCreate(10, sizeof(float));

// In control_task: send data to logger
float voltage = read_adc_voltage();
xQueueSendToBack(xDataQueue, &voltage, 0);  // non-blocking

// In logger_task: receive and log
float v;
if(xQueueReceive(xDataQueue, &v, portMAX_DELAY)) {
    log_to_sd(v);  // blocks until data available
}
```

**Mutexes** protect shared resources. **Semaphores** synchronize events. **Event groups** coordinate multiple tasks.

### Resources
- **FreeRTOS.org** — free official docs + "Mastering the FreeRTOS Kernel" e-book (free PDF, ~400 pages)
- **DigiKey "Intro to RTOS" YouTube series** — 15 episodes, starts from scratch, uses STM32 + FreeRTOS
- **STM32CubeIDE** — has built-in FreeRTOS integration via CMSIS-RTOS wrapper

### Milestones
- [ ] Two tasks running concurrently (different blink rates, no blocking each other)
- [ ] Queue passing data from ADC task to display/UART task
- [ ] Mutex protecting shared peripheral access (e.g., SPI bus shared between two tasks)
- [ ] Control loop task running at verified timing (1 kHz or 10 kHz confirmed via oscilloscope)

---

## Phase 4 — TI C2000 (Power Electronics DSP) (Month 10–18, 3–4 hrs/wk)

**Goal**: Run digital control on the MCU that's inside real EV inverters and industrial converters. This is the end-state for SiC/GaN power electronics career.

### Hardware
**TI C2000 LaunchPad F28379D** (~$50 at TI.com or Digi-Key). Dual-core 200 MHz Cortex-R4F DSP. This is the chip inside countless commercial power converters.

### Tools (all free)
- **Code Composer Studio (CCS)** — free from TI; C/C++ IDE + debugger
- **C2000 controlSUITE / C2000Ware** — free peripheral driver libraries from TI

### C2000 Academy (TI's free online course)
Go to training.ti.com and search "C2000 Academy." This is a structured, free, self-paced course that teaches the C2000 from GPIO through digital power control. It is the single best resource for this phase.

### Key C2000 concepts
**ePWM module** (enhanced PWM — designed for power electronics):
```c
// Configure ePWM1 for 100 kHz switching, up-count mode
EPwm1Regs.TBPRD = 200;               // period = 200 → 100 kHz (200 MHz / 200 / 1 = 1 MHz? check)
EPwm1Regs.TBCTR = 0;                 // clear counter
EPwm1Regs.TBCTL.bit.CTRMODE = 0;    // up-count mode
EPwm1Regs.AQCTLA.bit.ZRO = AQ_SET; // PWMA high at zero
EPwm1Regs.AQCTLA.bit.CAU = AQ_CLEAR; // PWMA low at compare A match
EPwm1Regs.CMPA.bit.CMPA = 100;     // 50% duty cycle
```

**ADC + PWM synchronization** (critical for power electronics control):
```c
// Trigger ADC at center of PWM period (TBCTR = TBPRD/2)
EPwm1Regs.ETSEL.bit.SOCASEL = ET_CTR_PRD;  // SOC on period event
EPwm1Regs.ETPS.bit.SOCAPRD = ET_1ST;        // every 1st event

// ADC ISR — runs every PWM period
__interrupt void adc_isr(void) {
    int16_t adc_val = AdcaResultRegs.ADCRESULT0;
    float vc = (float)adc_val * (3.3f / 4095.0f);  // convert to volts
    
    // PI control (update duty cycle)
    float error = setpoint - vc;
    integral += Ki * error;
    float duty = Kp * error + integral;
    duty = CLAMP(duty, 0, EPwm1Regs.TBPRD);
    EPwm1Regs.CMPA.bit.CMPA = (uint16_t)duty;
    
    // Clear interrupt flag
    AdcaRegs.ADCINTFLGCLR.bit.ADCINT1 = 1;
    PieCtrlRegs.PIEACK.all = PIEACK_GROUP1;
}
```

### MISRA-C basics to know
```c
// MISRA violation: implicit type conversion
int x = 3.7;     // implicitly converts float to int — MISRA violation

// MISRA compliant:
int x = (int)3.7;  // explicit cast

// MISRA violation: dynamic memory
char *buf = malloc(100);  // no malloc allowed in MISRA-C

// MISRA compliant:
char buf[100];    // stack allocation only
```

### Key projects for Phase 4
1. **Digital buck converter**: Use C2000 to implement closed-loop PI voltage control on a small (5W) buck converter. Verify with oscilloscope and Python data capture.
2. **Double pulse test (DPT) emulator**: Write C code that generates the DPT switching pattern for a SiC MOSFET (see [[EE Physical Side — Actionable Skill Plan]]). Even without real hardware, structuring the code demonstrates understanding.
3. **CAN bus communication**: Send telemetry (voltage, current, duty cycle) from C2000 to PC via CAN bus. Receive commands to adjust setpoint.

### Milestones
- [ ] C2000 LaunchPad blinking LED via C2000 GPIO registers (no HAL)
- [ ] ePWM configured and switching at correct frequency (verified on oscilloscope)
- [ ] ADC triggered by ePWM, ISR running at PWM rate
- [ ] Closed-loop PI control working on a real or simulated plant
- [ ] CAN bus message transmitted and received

---

## Combined C/C++ Timeline

| Month | Phase | Key output |
|-------|-------|-----------|
| 1–2 | Phase 0: C fundamentals | Pointer-fluent C programs; K&R exercises done |
| 2–4 | Phase 1: Arduino C++ | 5 extended projects; ADC, I2C, PWM, UART |
| 4–7 | Phase 2: STM32 HAL | Voltage logger system; PWM + ADC + UART working |
| 7–10 | Phase 3: FreeRTOS | Multi-task firmware; control loop at known rate |
| 10–18 | Phase 4: TI C2000 | Closed-loop power control; MISRA basics; CAN bus |

**For Joe's timeline**: Arduino bridges directly from [[EE Freshman Action Plans]] Action Plan 6. Phase 0 C fundamentals should start concurrently in Year 1. STM32 and beyond are Year 2–3 territory as EE coursework deepens.

---

## Resource Summary

| Resource | Cost | Phase |
|----------|------|-------|
| "The C Programming Language" K&R | ~$25 used | Phase 0 |
| CS50 (cs50.harvard.edu) | Free | Phase 0 |
| "Mastering STM32" by Noviello | ~$20 | Phase 2 |
| Jonathan Valvano STM32 textbook | Free (partial) | Phase 2 |
| FreeRTOS "Mastering" e-book | Free PDF | Phase 3 |
| DigiKey "Intro to RTOS" YouTube | Free | Phase 3 |
| TI C2000 Academy | Free | Phase 4 |
| cppreference.com | Free | All |
| embeddedartistry.com | Free | All phases |

---

## Related
- [[C++ in Electrical Engineering]]
- [[Python Self-Teaching Roadmap for EE]]
- [[EE Freshman Action Plans]]
- [[EE Physical Side — Actionable Skill Plan]]
- [[Research - Python and C++ in Electrical Engineering]]
- [[EE High Income Action Plan]]

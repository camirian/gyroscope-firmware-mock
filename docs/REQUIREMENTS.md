# Software Requirements Specification (SRS) - MEMS Gyroscope Firmware

**Assigned DAL:** Level A (DO-254 / DO-178C)
**Subsystem:** Attitude Determination System (SafeACS)

---

## 1. Functional Requirements

| Req ID | Requirement Text | Verification Method | Derived From |
| :--- | :--- | :--- | :--- |
| `REQ-GYRO-001` | The firmware shall initialize the SPI interface at 10 MHz. | Test | `SYS-REQ-104` |
| `REQ-GYRO-002` | The firmware shall command the gyroscope into active mode by writing `0x08` to `CTRL_REG1` (`0x10`). | Test | `SYS-REQ-105` |
| `REQ-GYRO-003` | The firmware shall read the `WHO_AM_I` register (`0x0F`) during initialization and verify a response of `0xD4`. | Test | `SYS-REQ-105` |
| `REQ-GYRO-004` | In the event `WHO_AM_I` does not return `0xD4`, the firmware shall transition the Attitude Subsystem to `FAULT_STATE`. | Analysis | `SYS-SAFE-012` |
| `REQ-GYRO-005` | The firmware shall poll the X, Y, and Z angular rate registers at a frequency of 100 Hz. | Test | `SYS-PERF-022` |

## 2. Performance Requirements

| Req ID | Requirement Text | Verification Method | Derived From |
| :--- | :--- | :--- | :--- |
| `REQ-GYRO-101` | Latency between SPI read completion and data availability to the control law shall not exceed 2 milliseconds. | Test | `SYS-PERF-023` |
| `REQ-GYRO-102` | The firmware shall apply the 16-bit to DPS scale factor (`0.00875`) using fixed-point arithmetic to prevent floating-point unit (FPU) stalls. | Analysis | `SYS-PERF-024` |

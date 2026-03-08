# Interface Control Document (ICD) - 3-Axis MEMS Gyroscope

**Document Control Number:** ICD-GYRO-001
**Revision:** A
**Target:** SafeACS Attitude Determination System

---

## 1. Physical Interface
**Protocol:** Serial Peripheral Interface (SPI)
**Clock Speed:** 10 MHz (Max)
**Data Frame Size:** 16-bit
**Voltage:** 3.3V CMOS

## 2. Register Map

| Address (Hex) | Register Name | R/W | Description | Default State |
| :--- | :--- | :--- | :--- | :--- |
| `0x0F` | `WHO_AM_I` | R | Device Identification (Constant: `0xD4`) | `0xD4` |
| `0x10` | `CTRL_REG1` | R/W | Power Mode & Data Rate | `0x00` (Power Down) |
| `0x11` | `CTRL_REG2` | R/W | High-Pass Filter Configuration | `0x00` |
| `0x22` | `OUT_X_L` | R | X-axis angular rate data (Low Byte) | `0x00` |
| `0x23` | `OUT_X_H` | R | X-axis angular rate data (High Byte) | `0x00` |
| `0x24` | `OUT_Y_L` | R | Y-axis angular rate data (Low Byte) | `0x00` |
| `0x25` | `OUT_Y_H` | R | Y-axis angular rate data (High Byte) | `0x00` |
| `0x26` | `OUT_Z_L` | R | Z-axis angular rate data (Low Byte) | `0x00` |
| `0x27` | `OUT_Z_H` | R | Z-axis angular rate data (High Byte) | `0x00` |

## 3. Data Formatting
Angular rate data is represented as 16-bit two's complement integers.
Conversion to physical units (Degrees Per Second - dps):
*   **Scale Factor:** `0.00875 dps / LSB` (at ±250 dps full scale)
*   `Rate_dps = Value_16bit * 0.00875`

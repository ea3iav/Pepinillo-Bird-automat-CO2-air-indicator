# Pepinillo-Bird-automat-CO2-air-indicator
yet another air quality bird project
# 🐦 CO₂ Canary Bird

A simple, physical air-quality indicator inspired by the historical concept of the “canary in the coal mine”.

This project visualizes indoor air quality using a small mechanical bird:

* When the air is **clean**, the bird stands upright 🟢
* When the air is **bad**, the bird “falls” 🔴

It is designed to be **simple, accessible, and low-power**, while still using a **real CO₂ sensor**.

---

## 🌍 Inspiration

This project is inspired by:

* The historical use of canaries in coal mines as early warning systems
* The work of Andy Warburton and similar ambient devices

However, the goal here was different:

> Make something **easy to build, understandable, and practical for everyday use**

So instead of a complex or highly polished object, this version focuses on:

* simplicity
* reproducibility
* accessibility

Additionally, this version includes:

* 🔋 **battery power** (for standalone use)
* 📦 a **larger enclosure** to house the battery and electronics

---

## 🧠 How it works

The system is based on:

* ESP32 (MicroPython)
* SCD41 (NDIR CO₂ sensor) (Swiss technology) ( I tried many VOC sensors, and they all were a compromise)
* SG90 servo (mechanical movement) 180 degrees model.

### Measurement cycle

* The device wakes up periodically
* Measures CO₂ concentration (ppm)
* Updates the bird position
* Goes back to deep sleep to save battery

---

## 🐦 Behaviour

The bird represents air quality:

| CO₂ (ppm) | Air quality | Bird       |
| --------- | ----------- | ---------- |
| < 1000    | Good        | Upright 🟢 |
| > 1200    | Bad         | Fallen 🔴  |

The system uses simple logic:

* Only moves when the state changes
* Smooth movement for a more natural feel

---

## ⚡ Power optimization

To maximize battery life:

* Deep sleep between measurements
* WiFi and Bluetooth disabled
* Servo only moves when needed

   🔋 Battery Voltage Monitoring (New Feature)
   
   This project now includes battery voltage monitoring using the ESP32’s ADC, allowing the system to:
   
   Detect when the LiPo battery is low
   
   Move the bird to a safe position (90°)
   
   YOU NEED TO CONECT THIS voltage divider. Otherwise use Main_no_batteryturn_off.py and change the name to main.py
  Enter deep sleep to prevent battery damage
            Two resistors are used:
          
          R1 = 100kΩ
          
          R2 = 100kΩ

    Connection:
       Battery + ---- R1 ----+---- R2 ---- GND
                             |
                         GPIO34 (ADC)
### Smart sampling

* First hour → measurements every **30 seconds**
* After that → every **120 seconds**

This allows:

* fast feedback when first powered on
* efficient long-term operation

---

## 🎯 Purpose

This device is not just a sensor — it's an **ambient interface**.

Instead of showing numbers on a screen, it answers a simple question:

> “Is the air OK right now?”

It encourages:

* better ventilation habits
* awareness of indoor air quality
* low-friction interaction

---

## 🛠️ Design philosophy

* Keep it **simple**
* Make it **buildable by anyone**
* Use **real data (CO₂)**
* Prefer **physical feedback over screens**

---

## 📦 Features

* Real CO₂ measurement (NDIR)
* Physical, intuitive feedback
* Battery-powered
* Low power consumption
* No app, no setup, no distractions

---

## 🚀 Future ideas

* Adaptive thresholds
* Multi-state behaviour (not just binary)
* Different motion patterns
* Data logging (optional)

---

## 📜 License

Open-source — feel free to build, modify, and improve.

---

## 🤝 Acknowledgements

* Inspired by historical canary systems
* Inspired by Canairi project
* Influenced by the work of Andy Warburton
* Built with a focus on simplicity and accessibility

---
## 📦 3D STL

* Bird parts https://www.printables.com/model/450447-birb-the-canary-shaped-air-quality-sensor/files
* Case: https://www.thingiverse.com/thing:7318502

🐦 *A small object that quietly tells you when it's time to open a window.*


EXTRA!!!

## 🚀 Flashing MicroPython on ESP32 using Thonny (Beginner Guide)

This guide explains how to install MicroPython on an ESP32 using Thonny — no command line required.

---

### 1️⃣ Install Thonny

Download and install Thonny:

👉 https://thonny.org/

Thonny includes everything you need (Python + tools).

---

### 2️⃣ Connect your ESP32

* Plug your ESP32 into your computer via USB
* Make sure your cable supports **data** (not just charging)

---

### 3️⃣ Open the MicroPython installer in Thonny

In Thonny:

* Go to **Tools → Options → Interpreter**
* Select:

  * **MicroPython (ESP32)**

Click **“Install or update MicroPython”**

---

### 4️⃣ Flash MicroPython

In the installer window:

* Select your ESP32 port (e.g. `COM3` or `/dev/ttyUSB0`)
* Choose the latest firmware (or browse manually)

👉 Firmware downloads:
https://micropython.org/download/esp32/

Click **Install**

Wait until it finishes.

---

### 5️⃣ Connect to the ESP32

After flashing:

* Go again to **Tools → Options → Interpreter**
* Select:

  * **MicroPython (ESP32)**
* Choose the correct port

You should now see the MicroPython REPL in Thonny.

---

### 6️⃣ Upload your code

* Open your `main.py` file
* Click **File → Save As…**
* Select **“MicroPython device”**
* Save it as:

```text
main.py
```

---

### ⚠️ Important: Auto-run behavior

When a file named `main.py` is present on the ESP32:

> It will automatically run every time the board powers on or resets.

This means:

* No need to press run
* Your project starts instantly
* It will also run after deep sleep

---

### 🛠️ Troubleshooting

#### ❌ Device not detected

* Try another USB cable
* Install drivers (CP210 / CH340)

#### ❌ Can't upload code (device keeps restarting)

* Press **STOP** in Thonny quickly after connecting
* Or hold the **BOOT** button while plugging in

#### ❌ Wrong port

* Check available ports in Thonny
* Reconnect the device


## 🐦 TRICK to understand the position of the bird. 
Try this code on a different window of Thonny and make it run, the console will display angle while it is moving so you can determine the ideal angle to place your Bird.

          from machine import Pin
          from sg90 import SG90
          import time
          
          servo = SG90(4)
          
          while True:
              print("0 grados")
              servo.set_angle(0)
              time.sleep(2)
          
              print("90 grados")
              servo.set_angle(90)
              time.sleep(2)
          
              print("180 grados")
              servo.set_angle(180)
              time.sleep(2)
---

### ✅ Done

If everything worked:

* MicroPython is installed
* Your `main.py` runs automatically
* Your ESP32 is ready to use 🐦


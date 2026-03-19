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
* SCD41 (NDIR CO₂ sensor) (Swiss technology)
* SG90 servo (mechanical movement)

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

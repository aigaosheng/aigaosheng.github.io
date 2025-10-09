---
layout: post
title: "Your Wi-Fi Can Now Listen to Your Heartbeat—No Wearables Required"
date: 2025-10-09 23:03:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Contactless health monitoring  
- Wi-Fi sensing  
- AI-powered diagnostics
---
---
**Your Wi-Fi Can Now Listen to Your Heartbeat—No Wearables Required**

Imagine this: you’re lounging on your couch after a long day, and without strapping on a smartwatch or clipping on a pulse oximeter, your heartbeat is being monitored in real time—by your Wi-Fi router. Sounds like sci-fi? It’s not. Thanks to a breakthrough from researchers at the University of California, Santa Cruz, your everyday Wi-Fi signals might soon double as a silent, invisible health guardian.

Meet **Pulse-Fi**—a clever, low-cost system that turns ambient Wi-Fi into a contactless vital signs monitor. Developed by Professor Katia Obraczka and her team, including postdoc Nayan Sanjay Bhatia and high school intern Pranay Kocheta, Pulse-Fi detects the subtle chest movements caused by your heartbeat by analyzing tiny fluctuations in Wi-Fi signal amplitude. No cameras. No wearables. Just the invisible waves already bouncing around your home.

### Why This Matters

Traditional heart rate monitoring often relies on wearables—devices that can be uncomfortable, expensive, or simply forgotten on the nightstand. Camera-based systems offer a contactless alternative but falter in low light and raise serious privacy concerns (who wants their webcam watching them 24/7?). Pulse-Fi sidesteps both issues. It works in the dark, respects your privacy, and runs on hardware that costs as little as **$5–$10** (ESP32 microcontrollers) or **$30** (Raspberry Pi).

In lab tests, Pulse-Fi achieved an error rate of **less than 1.5 beats per minute**—on par with clinical-grade reference devices. It remained accurate whether participants were sitting, standing, walking, or even running in place, and worked reliably up to **10 feet away**.

Even more impressively, the AI model behind Pulse-Fi isn’t just regurgitating training data—it **generalizes well to new environments**, meaning it can adapt to real-world settings it’s never seen before. That’s a big deal for practical deployment in homes, hospitals, or senior care facilities.

The team has only tested single-person scenarios so far, but they’re now piloting **multi-user detection** and exploring applications beyond heart rate—like monitoring **breathing patterns** and detecting **sleep apnea**.

### What’s Next?

Obraczka’s team is already laying the groundwork to **commercialize Pulse-Fi**, envisioning a future where your smart home doesn’t just control lights and thermostats—it keeps an eye on your health, quietly and continuously.

---

### Glossary

- **Wi-Fi Signal Amplitude**: The strength or intensity of a Wi-Fi radio wave; tiny changes in amplitude can be caused by physical movements, like the rise and fall of your chest during a heartbeat.  
- **ESP32**: A low-cost, low-power microcontroller chip commonly used in IoT (Internet of Things) projects; supports Wi-Fi and Bluetooth.  
- **Pulse Oximeter**: A medical device that clips onto a fingertip to measure heart rate and blood oxygen levels—used here as a benchmark for accuracy.  
- **Contactless Monitoring**: Health tracking that doesn’t require physical contact with the body, enhancing comfort and usability.  
- **Generalization (in AI)**: The ability of a machine learning model to perform accurately on new, unseen data—not just memorizing training examples.

---

**Source**: [IEEE Spectrum – Wi-Fi Signal Heartbeat Detection](https://spectrum.ieee.org/wi-fi-signal-heartbeat-detection)

# 🧟 Zomb-Kill: The Gamified Process Hunter

[![Kiroween Hackathon](https://img.shields.io/badge/Hackathon-Kiroween_2025-orange?style=flat-square&logo=ghost)](https://devpost.com/software/zomb-kill)
[![Built With Kiro](https://img.shields.io/badge/Built_With-Kiro_IDE-purple?style=flat-square)](https://kiro.dev)
[![Python](https://img.shields.io/badge/Made_with-Python-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"Why use Task Manager when you can use a Shotgun?"**

**Zomb-Kill** transforms your boring system administration into an 8-bit survival horror arcade game. It scans your actual computer for running processes, visualizes them as monsters based on their RAM usage, and lets you "kill" them to free up memory.

---

## 👻 What it Does
- **Scans System Processes:** Uses `psutil` to fetch real-time data about what is running on your machine.
- **Visualizes RAM Hoarders:** Processes are rendered as zombies. The more RAM they eat, the bigger their health bar.
- **Gamified Optimization:** Clicking a zombie sends a termination signal to the process, effectively killing the app and saving your computer resources.
- **Safety Protocol:** Includes filters to prevent you from accidentally killing critical System/Kernel tasks (no Blue Screens allowed!).

## ⚙️ Built With
- **Python 3.10+**
- **PyGame:** For the retro 8-bit rendering engine.
- **Psutil:** For system monitoring and process management.
- **Kiro IDE:** Used for 95% of the code generation (Vibe Coding & Steering Docs).

## 🛠️ Installation & Usage

### Prerequisites
- Python installed on your machine.

### Steps
1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/zomb-kill.git](https://github.com/YOUR_USERNAME/zomb-kill.git)
   cd zomb-kill
   
**2.Install Dependencies**
install -r requirements.txt

**3.Run the GameBash**
python main.py

**ControlsMouse:**
Aim the crosshair.
Left Click: Shoot zombie (Terminates Process).
ESC: Quit Game.

**🧠 How Kiro Was Used**
This project was built specifically for the Kiroween Hackathon to demonstrate the power of AI-assisted development.

**Feature How we used it**

**Vibe Coding -** Generated the backend logic. We asked Kiro to "Write a psutil script that outputs a JSON of processes formatted like RPG monsters," and it handled the complex system API calls automatically.
**Steering Docs -** We uploaded the PyGame documentation into Kiro's context. This allowed the AI to write a bug-free rendering loop and collision detection system without hallucinating non-existent methods.
**.kiro Specs -** We used a spec file (located in /.kiro/specs.md) to define the safety constraints, ensuring the AI knew never to target root processes.

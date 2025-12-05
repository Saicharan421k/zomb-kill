# Zomb-Kill Project Spec

## Goal
Create a gamified process manager using PyGame and Psutil.

## Components
1. **Backend (Vibe Coding):**
   - Use `psutil` to fetch process list.
   - Filter for user-level processes only.
   - Map memory usage (RSS) to "Monster Health".

2. **Frontend (Steering Docs):**
   - Initialize PyGame window (800x600).
   - Render "Zombies" as green sprites.
   - Implement "Shotgun" cursor logic.
   - On click -> Terminate process -> Play sound.

## Rules
- Do not kill System/Kernel processes.
- Visual style: 8-bit / CRT Monitor effect.

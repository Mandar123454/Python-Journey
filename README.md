# Python Journey 🐍

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Learning Path](https://img.shields.io/badge/Learning-Basics%20%E2%86%92%20Advanced-blue)

A curated, end‑to‑end Python learning journey covering fundamentals, intermediate and advanced concepts, file I/O, OOP, functional patterns, concurrency, and desktop GUI with Tkinter — capped with complete mini‑projects and utilities.

This repository contains 100+ numbered scripts from 01 → 101 plus supporting assets. It’s designed both as a learning path and a handy reference of runnable examples.

---

## Overview
- Purpose: Learn Python step‑by‑step with runnable examples
- Scope: Basics, Advanced, OOP, Functional, File I/O, Concurrency, GUI
- Explained: Every script includes in‑code explanations and practice‑ready snippets
- Projects: Games and utilities (Calculator, Text Editor, Clock, RPS, Quiz, Tic‑Tac‑Toe, Snake)
- Platform: Windows (PowerShell), cross‑platform friendly where applicable
- Free & Open Source: 0 rupees — MIT licensed

---

## Quick Start

### 1) Clone and set up env
```powershell
# From your desired folder
git clone https://github.com/Mandar123454/Python-Journey.git
Push-Location "Python-Journey";
python -m venv .venv;
. .\.venv\Scripts\Activate.ps1;
python -m pip install --upgrade pip;
if (Test-Path requirements.txt) { pip install -r requirements.txt }
```

### 2) Run examples
```powershell
# Run any numbered script
python "01_main.py"
python "38_Rock,Paper,Scissors Game.py"
python "99_Text Editor Program.py"
```

---

## Repository Map

- basics/: Core Python syntax and data types
- io/: File I/O and OS interactions
- oop/: Object‑oriented programming essentials
- functional/: Higher‑order functions and functional utilities
- concurrency/: Threads, daemons, multiprocessing
- gui/: Tkinter widgets, events, animations
- projects/: Complete mini‑apps and games

Note: In this repository, examples are directly at root as numbered `.py` files with supporting assets alongside them for simplicity.

---

## Learning Path (Concepts)

<details>
<summary><b>Foundations</b> — variables, strings, numbers, flow control</summary>

- 01_main.py
- 02_Variables.py
- 03_Multiple Assignment.py
- 04_String Methods.py
- 05_Type cast.py
- 06_User input.py
- 07_Math functions.py
- 08_String slicing.py
- 09_If.py
- 10_Logical Operators.py
- 11_While Loops.py
- 12_For Loops.py
- 13_Nested Loops.py
- 14_Break Contine Pass.py
- 15_Lists.py
- 16_2D Lists.py
- 17_Tuples.py
- 18_Sets.py
- 19_Dictionaries.py
- 20_Indexing.py
- 21_Functions.py
- 22_Return Statement.py
- 23_Keyword Arguments.py
- 24_Nested Function Calls.py
- 25_Variable Scope.py
- 26_Args.py
- 27_Kwargs.py
- 28_String Format.py
- 29_Random Numbers.py
- 30_Exception Handling.py
</details>

<details>
<summary><b>Modules, CLI & File I/O</b></summary>

- 31_File Detection.py
- 32_Read A File.py
- 33_Write A File.py
- 34_Copy A File.py
- 35_Move A File.py
- 36_Delete A File.py
- 37_Modules.py
- 62_If_Name_=='_main_'.py
- 95_Run With Command Prompt.py
- 96_Pip.py
- 97_ .py to exe.py
</details>

<details>
<summary><b>OOP & Advanced Python</b></summary>

- 40_Object Oriented Programming.py
- 41_Class Variables.py
- 42_Inheritance.py
- 43_Multilevel Inheritance.py
- 44_Multiple Inheritance.py
- 45_Method Overriding.py
- 46_Method Chaining.py
- 47_Super Function.py
- 48_Abstract Classes.py
- 49_Objects As Arguments.py
- 50_Duck Typing.py
- 51_Walrus Operator.py
- 52_Functions To Variables.py
- 53_Higher Order Functions.py
- 54_Lambda.py
- 55_Sort.py
- 56_Map.py
- 57_Filter.py
- 58_Reduce.py
- 59_List Comprehensions.py
- 60_Dictionary Comprehensions.py
- 61_Zip Function.py
</details>

<details>
<summary><b>Time, Threads, Processes</b></summary>

- 63_Time Module.py
- 64_Threading.py
- 65_Daemon Threads.py
- 66_Multiprocessing.py
</details>

<details>
<summary><b>GUI with Tkinter</b> — widgets, dialogs, layouts, events</summary>

- 67_GUI Windows.py
- 68_Labels.py
- 69_Buttons.py
- 70_Entrybox.py
- 71_Checkbox.py
- 72_Radio Buttons.py
- 73_Scale.py
- 74_Listbox.py
- 75_MessageBox.py
- 76_Colorchooser.py
- 77_Text Area.py
- 78_Open A File (File Dialog).py
- 79_Save A File (File Dialog).py
- 80_Menubar.py
- 81_Frames.py
- 82_New Windows.py
- 83_Windows Tabs.py
- 84_Grid.py
- 85_Progress Bar.py
- 86_Canvas.py
- 87_Keyboard Events.py
- 88_Mouse Events.py
- 89_Drag & Drop.py
- 90_.py
- 90_1.py
- 91_Animations.py
- 92_Multiple Animations.py
</details>

<details>
<summary><b>Network / Utilities</b></summary>

- 94_Send An Email.py
</details>

---

## Projects (Complete Mini‑Apps)

- 38_Rock,Paper,Scissors Game.py 🎮
- 39_Quiz Game.py 🧩
- 93_Clock Program.py ⏰
- 98_Calculator Program.py 🧮
- 99_Text Editor Program.py 📝
- 100_Tik Tac Toe Game.py ❌⭕
- 101_Snake Game.py 🐍

Supporting modules/assets (examples): `38.5_messages.py`, `41.5_car.py`, `42.5_car.py`, images under 68.x/69.x/70.x/72.x/73.x/74.x/81.x/91.x/92.x, text files like `79.5_Test.txt`, etc.

---

## User Guide

- Run any script directly: `python "<number>_<title>.py"`
- Some GUI examples expect images next to the script; keep structure intact
- For email example (94): set environment variables or edit the script for SMTP credentials before running
- Packaging (97): demonstrates converting `.py` → `.exe` on Windows (PyInstaller or similar)

### Common Tasks
```powershell
# Activate venv
. .\.venv\Scripts\Activate.ps1

# Install deps (if any)
pip install -r requirements.txt

# Run a script
python "100_Tik Tac Toe Game.py"
```

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

---


## Acknowledgements

- Tkinter for simple desktop GUIs
- Python standard library for batteries‑included modules
- Everyone who learns by building — keep going!

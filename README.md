# 🎮 Micro:bit Maze Workshop

**Micro:bit Maze Workshop** is a Python project designed to help you program your BBC Micro:bit and interact with it via VSCode, terminal or Webbrowser. The project uses [Poetry](https://python-poetry.org/) for dependency management, and it relies on the `microfs` library to facilitate file transfers to your Micro:bit.

---
## 🌐 Websites
A collection of useful links to get started with Micro:bit and MicroPython or to find more information about the project.

### Micro:bit:
- [Micro:bit](https://microbit.org/)
- [Micro:bit Python](https://python.microbit.org/)
- [Micro:bit Python API](https://microbit-micropython.readthedocs.io/en/latest/)
- [Micro:bit Python Documentation](https://microbit.org/get-started/user-guide/python/)
- [Micro python](https://github.com/micropython/micropython)
- [micro:bit Microsoft](https://makecode.microbit.org/)

### VSCode:
- [VScode Extension](https://marketplace.visualstudio.com/items/?itemName=MAKinteract.micro-bit-python)

### Terminal:
- [Poetry](https://python-poetry.org/)
- [Microfs](https://github.com/ntoll/microfs)
- [uFlash](https://github.com/ntoll/uflash)
- [microbit-cutebot-micropython](https://github.com/Krakenus/microbit-cutebot-micropython?tab=readme-ov-file)

---

## 🖥️ Usage with Visual Studio Code

We recommend using VS Code with the **micro:bit Python** extension (`makinteract.micro-bit-python`).

1. **Install the extension:** Open VS Code, go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`) and install `micro:bit Python`.
2. **Open Project:** In VS Code, select `File` > `Open Folder` and select your project directory.
3. **Connect Micro:bit:** Plug your Micro:bit into your computer via USB.
4. **Flash Code:** Use Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select **"Micro:bit Python: Flash sketch on micro:bit"**.
5. **Open REPL:** Use Command Palette and select **"Micro:bit Python: Open REPL"** to view output.

---

## 💻 Terminal Usage

### 📦 Installation

**Windows:**

Open PowerShell and run:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Restart your terminal after installation.

**macOS:**

Open Terminal and run:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Verify installation:
```bash
poetry --version
```

Install Project Dependencies:

Navigate to your project directory and install dependencies:
```bash
cd microbit-maze-workshop
poetry install
```

### 📤 Upload via USB

Connect your Micro:bit via USB and run:
```bash
poetry run ufs put main.py
```

### 🔍 View Output via Serial

**Windows:** Use PuTTY or Tera Term, connect to the Micro:bit COM port at `115200` baud.

**macOS:** Use Terminal:
```bash
screen /dev/tty.usbmodemXXXX 115200
```
Replace `usbmodemXXXX` with your Micro:bit port.

Press `Ctrl+C` to enter REPL, `Ctrl+D` to reboot the Micro:bit.

### 📶 Bluetooth Connection

Pair your Micro:bit using the official app and flash via Bluetooth.

---

## 🌐 Web Browser

You can also use the [Micro:bit Python Editor](https://python.microbit.org/v/3/project):

1. **Open Editor:** Visit [python.microbit.org](https://python.microbit.org/v/3/project).
2. **Paste your code:** Copy your `main.py` into the editor.
3. **Connect Micro:bit:** Click **"Connect"** to pair via USB/WebUSB.
4. **Flash:** Click **"Send to micro:bit"**.


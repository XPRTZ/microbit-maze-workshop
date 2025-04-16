

# Workshop micro:bit met # Cutebot
Tijdens deze workshop gaan we aan de slag met micro:bit in combinatie met de Cutebot. In de Git repository staan in de src folder twee mappen:

- cutebot-timing
- cutebot-gyro

## cutebot-timing
Om te kijken welke kant de robot op kan gaan draait de robot aan de hand van timing. Wanneer de robot op een "kruispunt" terecht komt kijkt de robot eerst of hij rechtdoor kan, vervolgens gaat hij links en rechts draaien om te controleren of er een lijn is. De robot draait maximaal voor een vooraf geconfigureerde tijd. Deze tijd is geconfigureerd in MAX_DIRECTION_CHECK_TIME. Wanneer er geen lijn is gevonden draait de robot terug en gaat hij een andere kant controleren. Tijdens het draaien wordt pas na een bepaalde tijd gecontroleerd of er een lijn is. Deze waarde is geconfigureerd in DIRECTION_CHECK_DELAY. Dit is om ervoor te zorgen dat de huidige lijn niet als optie wordt gezien wanneer links of rechts gecontroleerd wordt. Afhankelijk van de baterijstatus kunnen de SPEED en de DRIVE_WHILE_LOST_LINE_TIME aangepast worden. Hoe voller de batterij, hoe lager de speed. De DRIVE_WHILE_LOST_LINE_TIME wordt gebruikt om nog een klein stukje door te rijden wanneer de lijn niet meer gezien wordt.

## cutebot-gyro
Om gebruik te maken van deze versie moet de GY-271 aangesloten worden. Het interne kompas van de micro:bit kan alleen gebruikt worden wanneer dit bordje horizontaal is aangesloten. Op de cutecar gaat dit niet. Net als bij de cutebot-timing zijn hier ook de SPEED en de DRIVE_WHILE_LOST_LINE_TIME van toepassing.

Deze versie maakt gebruik van het kompas om te draaien en weer terug te draaien. In theorie zou dit betrouwbaarder moeten zijn dan de timing versie. Het kompas moet echter wel zover mogelijk van de cutebot geplaatst worden om te interferentie te voorkomen. Het kompas lijkt hier erg gevoelig voor te zijn.

### Verbeteringen en uitdagingen
- Maak gebruik van de ultrasonic sensor om muren te herkennen
- Het doolhof is een 7x7 grid, probeer de kortste weg te vinden.
- Herken andere robots in het doolhof
- Herkennen uitgang doolhof (ultrasonic sensor kan ver kijken > 100cm)

## 🌐 Websites
A collection of useful links to get started with Micro:bit and MicroPython or to find more information about the project.

### Micro:bit:
- [Micro:bit](https://microbit.org/)
- [Micro:bit Python](https://python.microbit.org/)
- [Micro:bit Python API](https://microbit-micropython.readthedocs.io/en/latest/)
- [Micro:bit Python Documentation](https://microbit.org/get-started/user-guide/python/)
- [Micro python](https://github.com/micropython/micropython)
- [micro:bit Microsoft](https://makecode.microbit.org/)
- [Cutebot robot](https://elecfreaks.com/learn-en/microbitKit/smart_cutebot/index.html)
- [Smart Cutebot Samples for Python](https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot-python.html)

### VSCode:
- [VScode Extension](https://marketplace.visualstudio.com/items/?itemName=MAKinteract.micro-bit-python)

### Terminal:
- [Poetry](https://python-poetry.org/)
- [Microfs](https://github.com/ntoll/microfs)
- [uFlash](https://github.com/ntoll/uflash)
- [microbit-cutebot-micropython](https://github.com/Krakenus/microbit-cutebot-micropython?tab=readme-ov-file)

## IDE
Code schrijven en deployen op de micro:bit kan op verschillende manieren. 
 
## 🖥️ Usage with Visual Studio Code

We recommend using VS Code with the **micro:bit Python** extension (`makinteract.micro-bit-python`).

1. **Install the extension:** Open VS Code, go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`) and install `micro:bit Python`.
2. **Open Project:** In VS Code, select `File` > `Open Folder` and select your project directory.
3. **Connect Micro:bit:** Plug your Micro:bit into your computer via USB.
4. **Flash Code:** Use Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select **"Micro:bit Python: Flash sketch on micro:bit"**.
5. **Open REPL:** Use Command Palette and select **"Micro:bit Python: Open REPL"** to view output.


## 🌐 Web Browser

You can also use the [Micro:bit Python Editor](https://python.microbit.org/v/3/project):

1. **Open Editor:** Visit [python.microbit.org](https://python.microbit.org/v/3/project).
2. **Paste your code:** Copy your `main.py` into the editor.
3. **Connect Micro:bit:** Click **"Connect"** to pair via USB/WebUSB.
4. **Flash:** Click **"Send to micro:bit"**.

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







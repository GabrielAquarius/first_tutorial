### README

## About this repository

This repository contains the **first game I coded using Pygame**, built by following **DaFluffyPotato’s tutorial**.

- **All code and assets belong to DaFluffyPotato.**
- I followed the tutorial entirely **for learning purposes**.
- I made a few **small changes** to improve code efficiency and/or reduce the number of lines of code.

## Building an executable with PyInstaller (step-by-step)

These steps package the game into a runnable executable.

### 1) Install PyInstaller

```bash
pip install -U pyinstaller
```

### 2) Run PyInstaller in your project folder

Open a terminal **in the root directory of the project** (where `game.py` is located), then run one of the commands below depending on your system/shell.

#### PowerShell (Windows)

```powershell
pyinstaller game.py --noconsole --onefile
```

#### Command Prompt (Windows)

```bat
pyinstaller game.py --noconsole --onefile
```

#### Linux (bash)

```bash
pyinstaller game.py --noconsole --onefile
```

After running, PyInstaller will generate folders like `build/` and `dist/`, plus a `.spec` file.

### 3) Copy required folders into `dist/`

To ensure the packaged game runs correctly, copy the following into the `dist` folder (next to the generated executable):

- `Assets/`
- `Scripts/`
- `Pasta/`

Your `dist/` folder should end up looking roughly like this:

- `dist/`
  - `game` (Linux) or `game.exe` (Windows)
  - `Assets/`
  - `Scripts/`
  - `Pasta/`

### 4) Run the game

Run the executable inside `dist/`:

- Windows: double-click `game.exe`
- Linux: run `./game` from a terminal inside `dist/`

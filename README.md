# 🐭 So Long

A grid-based 2D Python maze game where you guide a mouse to collect cheese and find its way home!

```
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▄ █▀▄▄▀████ ████▀▄▄▀█ ▄▄▀█ ▄▄▄
██▄▄▄▀▀█ ██ ████ ████ ██ █ ██ █ █▄▀
██ ▀▀▀ ██▄▄█████ ▀▀ ██▄▄██▄██▄█▄▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
```

## 📝 Description

A text-based maze game written in Python where players navigate through a maze using WASD controls. The game features emoji-based graphics, collectible items, and path-finding challenges.

## 🎮 Game Elements

- 🐭 Player (P): Your character
- 🧀 Collectibles (C): Cheese to collect
- ⛳ Exit (E): The goal
- ❎ Walls (1): Barriers
- ⬛ Path (0): Empty spaces

## 🗺️ Map Requirements

Maps must follow these rules:
- Contains exactly 1 exit (E)
- Contains at least 1 collectible (C)
- Contains exactly 1 starting position (P)
- Must be rectangular
- Must have a valid path from start to exit
- Must be surrounded by walls
- No duplicate exits or starting positions

## 🚀 How to Play

1. Run the game:
```bash
python main.py
```

2. Controls:
- W: Move North
- A: Move West
- S: Move South
- D: Move East

3. Objective:
- Collect all the cheese (🧀)
- Find your way to the goal (⛳)
- Complete the maze in as few moves as possible!

## 📋 Map Format

Create your own maps in a text file (e.g., `map.txt`) using these symbols:
```
1111111111
1P000C0001
100011C001
1C00110001
1111E11111
```

Where:
- 1: Wall
- 0: Empty path
- P: Player starting position
- C: Collectible
- E: Exit

## 🛠️ Requirements

- Python 3.x
- Operating System: Windows/Linux/MacOS
- Terminal that supports emoji display

## 📊 Features

- Emoji-based graphics
- Move counter
- Collectible item tracking
- Clear screen functionality for smooth gameplay
- Directional feedback
- Win condition checking
- Valid map verification

## 🎯 Future Enhancements

- Map Checker - must have path to exit
- Move tracking
- Sound effects
- More complex map elements

## 👤 Author

- myuen (42 Singapore)

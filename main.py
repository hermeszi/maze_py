'''
Map Validation Checklist:
 Map contains 1 exit (E).
 Map contains at least 1 collectible (C).
 Map contains 1 starting position (P).
 No duplicate exit (E) or starting position (P).
- If duplicates are found, display an error message.

 Map is rectangular.
 Valid path exists from the start (P) to the exit (E).
 Map is surrounded by walls (1) (closed map). - If the map is not surrounded by walls, return an error.
 -Map respects all the above rules for any valid input. If not, display an error message.
'''

import os

def flood_fill(game_map, x, y):
    if map_copy[x+1][y] == 'F' or map_copy[x+1][y] == '1':
        return
    else:
        floor_fill()

# Title
TITLE = '''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▄ █▀▄▄▀████ ████▀▄▄▀█ ▄▄▀█ ▄▄▄
██▄▄▄▀▀█ ██ ████ ████ ██ █ ██ █ █▄▀
██ ▀▀▀ ██▄▄█████ ▀▀ ██▄▄██▄██▄█▄▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
'''
print(TITLE)
print("    █▓▒▒░░░A 2D Game░░░▒▒▓█    ")
print("ヽ༼ʘ̚ل͜ʘ̚༽ﾉ      ୧༼ʘ̆ںʘ̆༽୨     ༼:◕:ل͜◕:༽    ヽ༼ຈل͜ຈ༽ﾉ")
print()

# Define the emoji "skin" mapping
emoji_mapping = {
    '1': '❎',  # Wall
    '0': '⬛',  # Empty path
    'P': '🐭',  # Player
    'C': '🧀',  # Collectable
    'E': '⛳'    # Home (Goal)
}

# Read the map from the file and find the player's initial position (marked by 'P')
def read_map(filename):
    array = []
    player_pos = None
    with open(filename, 'r') as file:
        for y, line in enumerate(file):
            row = list(line.strip())  # Create a list of characters from each line
            if 'P' in row:  # Check if 'P' is in the row
                x = row.index('P')  # Find the position of 'P' in the row
                player_pos = (x, y)  # Store the player's position (x, y)
                row[x] = '0'  # Replace 'P' with an empty tile ('0')
            array.append(row)
    return array, player_pos

# Function to draw the map with the player, using emojis
def draw_map(game_map, player_pos):
    # Make a copy of the map to display the player without modifying the original map
    map_copy = [row.copy() for row in game_map]

    # Place the player on the map
    px, py = player_pos
    map_copy[py][px] = 'P'  # 'P' represents the player

    # Draw the map with emojis
    for row in map_copy:
        for c in row:
            # Use the emoji_mapping to replace each character with its corresponding emoji
            print(emoji_mapping.get(c, c), end='')  # Default to character if no mapping exists
        print()  # Newline after each row

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Example usage:
filename = 'map.txt'
game_map, player_pos = read_map(filename)

# Initialize move counter and collected items counter
move_count = 0
items_collected = 0

# Draw the initial map with player
draw_map(game_map, player_pos)

# Game loop
while True:
    move = input("Move (W, A, S, D): ").strip().upper()

    # Get the current player position
    px, py = player_pos

    # Update player position based on input
    if move == 'A' and px > 0 and game_map[py][px - 1] != '1':  # Move left (West)
        px -= 1
        print("You journey West")
    elif move == 'D' and px < len(game_map[0]) - 1 and game_map[py][px + 1] != '1':  # Move right (East)
        px += 1
        print("You move cautiously East")
    elif move == 'W' and py > 0 and game_map[py - 1][px] != '1':  # Move up (North)
        py -= 1
        print("You head North")
    elif move == 'S' and py < len(game_map) - 1 and game_map[py + 1][px] != '1':  # Move down (South)
        py += 1
        print("You move South")

    # Check for collectables ('C') at the new player position
    if game_map[py][px] == 'C':
        print("You collected a 🧀!")
        items_collected += 1
        game_map[py][px] = '0'  # Replace 'C' with '0' after collecting

    # Check if player reached the goal ('E')
    if game_map[py][px] == 'E':
        print("You reached the goal! 🏁")
        break

    # Increment move count after each move
    move_count += 1

    # Update the player's position
    player_pos = (px, py)

    # Clear the screen before redrawing the map
    clear_screen()

    # Redraw the map with the updated player position
    draw_map(game_map, player_pos)

# After the game ends, print the final stats
print(f"Game over! You made {move_count} moves and collected {items_collected} items.")

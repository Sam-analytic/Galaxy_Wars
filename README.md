# Galaxy_Wars
Semester Project developed using Pygame  - Galaxy Wars. 	
Try to shoot your opponent and gain as much points as possible before the time is up. But wait, do your bullets travel straight anymore or do you have to account for gravity?

# Modes:

PvP only on local network.

# Objects:

1. Space ships - one for each player. Move up and down and shoot with left mouse button.
2. Planets in middle - deflect bullets with their gravity - hard to shoot your opponent.
3. Score boards at bottom - keep track of scores during the game. 

# INTERACTION -
1. Key W --- Ship moves up
2. Key S --- Ship moves down
3. Left mouse button --- ship shoots 


# DEV PLAN:

The game can be divided into mainly two parts - objects and interactions.
The objects can be further divided into two many classes under two main modules  - environment and gameplayinterface and gameplayobjects.
The interaction can also be divided into the following - In game interaction and game screen, main menu interaction. 
All the player's high scores against the CPU are saved on a file created during the game time.
Player vs player mode is connected over the internet - with each player on a different computer. 

# How to play:
1. You need 2 people 
2. connect to same wifi
3. open mfr1 and mfr2 files on different computers 
4. Player 2 (with mfr2) needs to fix his ip -- the program asks for this before starting as - "Please enter the connection IP address: "
5. Play)

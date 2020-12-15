# Galaxy_Wars
Semester Project developed using Pygame  - Galaxy Wars.

NOTE: I think that this game can be easily developed with a standard object oriented Framwork.

GAMEPLAY: (Alpha version)

Modes:

PvP only on local network.

Objects:

1. Space ships - one for each player. Move up and down and shoot with left mouse button.
2. Planets in middle - deflect bullets with their gravity - hard to shoot your opponent.
3. Score boards at bottom - keep track of scores during the game. 

INTERACTION -
Key W --- Ship moves up
Key S --- Ship moves down
Left mouse button --- ship shoots 


DEV PLAN:

The game can be divided into mainly two parts - objects and interactions.
The objects can be further divided into two many classes under two main modules  - environment and gameplayinterface and gameplayobjects.
The interaction can also be divided into the following - In game interaction and game screen, main menu interaction. 
All the player's high scores against the CPU are saved on a file created during the game time.
Player vs player mode is connected over the internet - with each player on a different computer. 

How to play:
1. You need 2 people 
2. connect to same wifi
3. open mfr1 and mfr2 files on different computers 
4. Player 2 (with mfr2) needs to fix his ip -- the program asks for this before starting as - "Please enter the connection IP address: "
4. play)

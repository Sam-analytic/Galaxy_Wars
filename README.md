# Galaxy_Wars
Semester Project developed using Pygame  - Galaxy Wars.

NOTE: I think that this game can be easily developed with a standard object oriented Framwork.

GAMEPLAY: (Alpha version)

Modes:

PvP only on local network.

Objects:

1. Space ships (main objects, can move up down, left right on the screen, top down view on 2d screen, ships rotate with the keys (events) to point towards aim

Ships have attributes health and shield health (deflectors for laser weapons).

2. Black holes, worm hole (owned by the players, teleports weapons to the other player more directly, stays active for three turns once activated, two sided), stars, planets (all deflect weapons with different degree under a certain radius (newton’s law), nebula (no deflection but decreases the intensity of the weapon’s damage).

3. Basic Ammunition - Lasers, Direct aim Torpedos, Lock down torpedos (range of radius 60 pixels, 40 pixels,etc), Radar jammers (if hit properly, makes the ship invisible to the opponent), cloakers, add more…., surprise weapon on 0.5 probability that invites a random attacking spaceship for one turn if the wormhole is active. 
Weapons are chosen by players in a set of 5 to 8 frmo each - Low intensity, Medium intensity and High intensity weapons.

BACKGROUND:

Black with stars and cosmic dust here and there. The size of ships will be comparable to small blackholes since are not going to make it scale size exactly. The screen object sizes can also vary (by refactoring)

4. Panel for each player. Contains health of the ship, shield and the weapons avaialable.

MAIN SCREEN – 1. Start 1 player

2. Start 2 player

INTERACTION - 
Mostly stationary with some slight background digital twinkling of stars (using random numbers). The only interaction during game time would be - movement of ships during a particular time, weapons animation, and in game messages. 


DEV PLAN:

The game can be divided into mainly two parts - objects and interactions.
The objects can be further divided into two many classes under two main modules  - environment and gameplayinterface and gameplayobjects.
The interaction can also be divided into the following - In game interaction and game screen, main menu interaction. 
All the player's high scores against the CPU are saved on a file created during the game time.
Player vs player mode is connected over the internet - with each player on a different computer. 

How to play:
1. You need 2 people 
2. connect to same wifi
3. open mfr1 and mfr2 files on different computers and dont forget to change your ip in code
4. play)

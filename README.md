Space invaders assignment COM4023-PR1
by Aisha Asghar, Harry Hughes & Joshua Walker 

# Assignment abstract
- build a basic space invaders game using pygame, documenting and displaying the process for design and development as a team
- ensuring design and development decisions are justified
- using version control effectively so that the codebase is updated regularly and collaboratively throughout the process 

space invaders is a game where:
- the **player** is able to **move from side to side** 
- the player **attacks** aliens and gain points 
- **aliens attack** the player in order to reduce the number of lives to zero
- aliens get **faster** as the game progresses

# Requirements & technologies
## Examples & Existing solutions
- https://freeinvaders.org/
### Features and observations
- title screen
- sound effects
- aliens move forward as time progresses
- player lives reset for each wave
- enemies shoot different types of bullets
## Core features
### 1. Aliens
- must have 3 types
- must move from side to side
- fire at the player randomly
- movement speed increases as game progresses
### 2. Player
- should be able to attack (shoot bullets) at the aliens
	- bullets should kill aliens on contact
- should lose a life upon being hit with an enemy bullet
### 3. Barriers
- must have 4 barriers
- barriers must degrade/ lose "health" as they are shot at
	- should take damage from both alien and player bullets
### Allocation of Features
- Aisha: Barriers
- Harry: Player
- Joshua: Aliens
## Bonus Features 
- features that don't have to be implemented to fulfill the requirements
### 1. Aliens
- when all the current aliens have been defeated, a new wave should spawn
- aliens can shoot different types of bullets in addition to the regular types of bullet
	- instant-kill bullets (take all player lives in one go)
	- paralyze bullets (cause the player to be unable to move/ shoot for a short period of time)
	- slow bullets (reduce player speed for a short period of time)
- different types of aliens may have different score values 
### 2. Player
- player can collect power-ups
	- increase speed
	- extra life
	- double bullets
### 3. Barriers
- player can collect powerup to restore damaged barriers
### 4. QoL
- home screen
- pause button
- sound effects
- difficulty modes
	- eg a hard mode with no barrier
- track and display the player's score based on the number of enemies killed 
## tools
- must be written in python using pygame
	- python 3.13: widely available and easier to install on work laptops
	- using pygame-ce (a community-maintained fork of pygame) since the original pygame does not support python versions beyond python 3.8

# Design

## Classes
### Player
Attributes:
	- lives
	- speed
### Aliens
Attributes:
	- point value
	- speed
	- type
### Bullets
Attributes:
	type (?)
### Barrier
- barriers can be implemented as 4 clusters of individual barrier blocks
- each "barrier block" can be an instance of the barrier class
Attributes:
	- health

# Development & testing
- development and version control will be tracked using Github:
	https://github.com/Aiii-1111/com4023-pr1

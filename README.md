# Hack_Sprint-Breakfast
This repo holds the pygame "Rise and Dine: Wes's Cozy Kitchen" built for our Holberton Hack Sprint

"Rise and Dine: Wes's Cozy Kitchen" is a single player breakfast ingredient choosing game developed using [pygame](https://www.pygame.org/news) featuring a retro theme and chill gameplay with a focus on the player's choice of ingredients and how they affect the breakfast meal chosen by the Chef.

## Index

- [Installation](#installation)
- [Game details](#game-details)
- [Settings](#settings)
- [Technical info](#technical-info)
- [Credits](#credits)

<h1 id="installation">Installation</h1>

> Installing Title of the Game takes 4 easy steps: **(You will need git installed to do this!)**
> 1. Create a new folder
> 2. Open a command line and use `cd` to move to the created folder
> 3. Type `git init` and hit enter
> 4. Type `git clone add repo here` and hit enter

As python is commonly already installed on most systems by default, it should run without manual installation of  
python. Furthermore, if the game is launched and fails to `import pygame` then a prompt will show and ask the  
user to try and automatically install it for them to minimise hassle. If all else fails, the user will have to manually  
install `pygame` to be able to play the game.

<h1 id="game-details">Game details</h1>

"Rise and Dine: Wes's Cozy Kitchen" 
The game was created as a Hack Sprint themed project for the Holberton School Software Engineering School,  
where the theme was 'Breakfast'. Students were given 1 week to create something related to the theme. This could be a website,
and application, or whatever the group would like to work on and demostrate some skills.

The game is a single player game where the player is given a choice of ingredients to choose from,
and the player must choose the correct ingredient to match the meal that the Chef is making for the current level.

As this game is only 2D and runs purely in Python 3, it is very performant and has several features to try and improve  
on the amount of processing power this game needs to run such as slowing down screen updates if the user tabs out  
which dramatically decreases the amount of processing the game uses when it is running.

## Levels

There are 10 Levels that the player can play through currently, each with a different meal that the player must match according to
our Chef name Wes. All of the meals are breakfast meals and get progressively harder as the player progresses through the
levels to pick the correct ingredients.

ADD PICTURES HERE

<h1 id="technical-info">Technical info</h1>

## File structure

This game is built purely in python and only has one dependency that doesn't come with python and that is  
`import pygame`. 


All of these files are located within bla bla bla

## Display & resolution management

To allow the game to support multiple resolutions with the least amount of code, I have designed my own system where the game  
never directly draws to the screen with assets or text, the user is always looking at the `Window` which is different from the `Display`,  
as `Window` is a `pygame.surface.Surface` that all the game is drawn to, then when the screen needs updating the `Window` is scaled  
to the `Display` and updates either the entire screen or specific parts that have changed for performance.


<h1 id="credits">Credits</h1>

- Dominick <https://github.com/DominickKeeling>
- Robert Farley <https://github.com/Nomad-Rob>
- Shadi Shwiyat <https://github.com/Shadi-Shwiyat>

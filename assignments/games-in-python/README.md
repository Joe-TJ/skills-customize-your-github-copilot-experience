# 📘 Assignment: Games in Python

## 🎯 Objective

Build a text-based Hangman game to practice core Python programming skills. In this assignment, you will use loops, conditionals, strings, and user input to create a complete playable game.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create the initial game setup by defining a list of possible words, choosing one word at random, and preparing variables to track guesses and remaining attempts.

#### Requirements
Completed program should:

- Store at least 5 possible secret words in a list.
- Randomly choose one secret word at the start of the game.
- Create a display state using underscores for unguessed letters.
- Initialize a counter for incorrect guesses remaining.


### 🛠️ Guess Processing and Win/Lose Logic

#### Description
Implement the game loop that asks the player for letter guesses, updates progress, tracks mistakes, and ends the game with the correct result message.

#### Requirements
Completed program should:

- Prompt the player to enter one letter each turn.
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining attempts only for incorrect guesses.
- End with a win message when all letters are guessed.
- End with a lose message when attempts reach zero and show the secret word.

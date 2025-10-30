
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a console-based Hangman game that reinforces string manipulation, looping, conditionals, and user input handling. Students will implement game state tracking (revealed letters, wrong guesses, remaining attempts) and produce clear win/lose output.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a playable Hangman program in Python. The program should select a secret word at random from a predefined list, display masked progress to the player, accept single-letter guesses (case-insensitive), and end when the player either guesses the full word or exhausts the allowed number of incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the current word progress in a spaced `_ _ a _ _` format
- Accept single-letter guesses from the user (case-insensitive)
- Track and display the number of incorrect guesses remaining (e.g., 6 attempts)
- Prevent repeated penalty for the same incorrect guess
- Show letters that have already been guessed (correct and incorrect)
- End with a clear win or lose message and reveal the secret word on loss
- Include brief usage instructions or comments in your code

#### Example interaction
```
Welcome to Hangman!
Word: _ _ _ _ _
Guesses left: 6
Guessed letters: 
Enter your guess: a
Good guess! Word: _ a _ _ _
Guesses left: 6
Guessed letters: a
Enter your guess: z
Sorry, 'z' is not in the word.
Guesses left: 5
Guessed letters: a, z
```

---

Tip: A starter file `starter-code.py` is provided in this folder. Update or replace it with your final solution. Commit your final `.py` file to `assignments/games-in-python/` when submitting.

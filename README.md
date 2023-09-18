### Copyright (C) 2023 Anthony Ryan Shannon/Ars Artis Softworks

# TRIVIA TREK: LETTER LABYRINTH

    An interactive text-based adventure that challenges your trivia knowledge and wits. In this game, you find yourself trapped within a mysterious labyrinth. To escape, you must navigate through a series of rooms, answering trivia questions, collecting letters, and ultimately solving a word-scramble puzzle. Can you overcome the challenges and escape the labyrinth?

    Demo: https://youtu.be/C-HsTyU6BgE

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Files Included:

    - 'trivia_trek.py':
        Main program file. Handles all primary game mechanics, including loading questions, scrambling word-scramble words, validating the sequence of scrambled letters to avoid prior adjacency, playing the rounds, and executing the final puzzle.

    - 'test_trivia_trek.py':
        File used to test each function of the main program using Pytest

    - 'README.md':
        You're reading it

    - 'requirements.txt':
        List of required modules

    - 'csv' folder:
        Folder of CSV files containing data for trivia questions and word-scramble puzzles

        - 'scramble_words.csv':
            List of 15-letter words and phrases for use in word scramble puzzles, with associated clues

        - 'geography.csv':
            List of geography trivia questions of three difficulty levels, with answer choices

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Dependencies:

    - pyfiglet

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## How to Launch:

    1. Execute the program via Python interpreter. Navigate to the code's directory and employ the command:

        python trivia_trek.py

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## How to Play:

    1. Initialization:

        Launch the program to begin your adventure. You'll be prompted to provide your name and select a trivia category.
            Categories currently supported:
                - geography

    2. Trivia Quest:

        As you enter each room, a series of doors await you, each corresponding to a different difficulty level. Your choice will determine the difficulty of the trivia question you receive. Correct answers yield points used to track your progress, as well as letters essential for the final phase.

    3. Final Chamber:

        Upon amassing sufficient points, you will reach the labyrinth's final chamber. Here, a word-scramble puzzle awaits, the culmination of your journey. Use your accumulated letters to unscramble the mystery word or phrase. You have two oppotrunities to succeed, with a clue available if needed.

    4. Escape or Consequences:

        Success in solving the final puzzle leads to escape from the labyrinth. Failure, however, carries its own dire consequences.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Game Mechanics:

    - The game's trivia questions derive from CSV files. Currently, the game only supports the "geography" category.

    - Questions are sorted by distinct difficulty levels. Your chosen door will define the question's difficulty.

    - Accurate answers yield letters that you'll employ during final puzzle phase.

    - The climactic puzzle involves deciphering a scrambled word or phrase. Draw upon your amassed letters and a provided clue to deduce the correct answer. Two attempts are at your disposal.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Customization:

    Exercise your creative freedom by introducing extra trivia categories and questions in new CSV files, and new word-scramble puzzles in the 'scramble_words.csv' file in the 'csv' folder.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Future Improvements:

    Content:

        - More trivia categories and questions
        - More word-scramble puzzles

    Mechanics:

        - Ask for three categories at the beginning of the game. When player chooses a door in each room, the category tied to that door is randomized from among the three chosen categories.
        - Visualization of progress through maze.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## License:

    GPL-3.0

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Credits:

     Thanks to:
     - David Malan and the Harvard cs50 crew for laying the knowledge foundations for this project.

     - Microsoft and the team behind Encarta's MindMaze for serving as the partial inspiration for this project.

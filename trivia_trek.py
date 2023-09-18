# Copyright (C) 2023 Anthony Ryan Shannon/Ars Artis Softworks

import csv
import random

from pyfiglet import Figlet


def main():
    # Create list to store available categories
    categories = [
        "geography",
    ]

    # Print title
    title = "Trivia Trek: Letter Labyrinth"
    print_title(title)

    # Prompt player for name
    name = input("What is your name? ")

    # Get questions from database based on user input of category
    while True:
        category = input(f"\nGreetings, {name}! What category would you prefer? ").lower()
        if category not in categories:
            print(f"Invalid category. Available categories: {categories}")
            continue
        else:
            break

    questions = load_questions(category)

    original_word, scrambled_letters, scramble_clue = scramble_letters()

    # Play first phase of the game (the trivia maze)
    score = 0
    letters_collected = []
    asked_questions = []

    # Continue playing rounds until score reaches 15
    while score < 15:
        score, letters_collected, scrambled_letters, asked_questions = play_round(
            questions, category, score, letters_collected, scrambled_letters, asked_questions
        )

    # Play second phase of the game (the final dungeon word scramble) and handle final outcome
    final_outcome = final_puzzle(original_word, letters_collected, scramble_clue)

    # Display outcome based on player's success
    if final_outcome == True:
        print(f"\nThe table sinks into the floor and the letters flash an other-worldly golden light.\nYou hear mechanisms in the walls come to life as the door across from you opens.\n\nCongratulations {name}! You have escaped the labyrinth!")
    else:
        print(f"\nThe table sinks into the floor and the letters flash an other-worldly crimson light.\nYou hear mechanisms in the walls come to life as the door behind you slams shut and the walls slowly close in on you.\n\nSorry, {name}. You failed to escape the labyrinth.")


# Prints title in FIGlet font
def print_title(title):
    f = Figlet(font="gothic")
    print(f.renderText(title))


# Handles loading trivia questions from data structure. Returns list or dictionary of questions for the game.
def load_questions(category):
    # Initialize empty dictionary to store trivia questions
    trivia_questions = {}

    # Open the CSV file (and close automatically when with block exited)
    with open(f"csv/{category}.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        # For each row in the CSV file:
        for row in reader:
            # Extract 'topic', 'question', 'choices', 'correct_choice', and 'level'
            topic = row["topic"]
            question = row["question"]
            choices = [row["choice1"], row["choice2"], row["choice3"], row["choice4"]]
            correct_choice = row["correct_choice"]
            level = row["level"]

            # If 'topic' is not in 'trivia_questions':
            if topic not in trivia_questions:
                # Add 'topic' to 'trivia_questions' with a value of a new dictionary with keys '1', '2', and '3', each with an empty list as a value
                trivia_questions[topic] = {"1": [], "2": [], "3": []}

            # Create a dictionary 'question_dict" with keys 'question', 'choices', 'correct_choice'
            question_dict = {
                "question": question,
                "choices": choices,
                "correct_choice": correct_choice,
            }

            # Append 'question_dict' to the appropriate list in 'trivia_questions' based on 'level'
            trivia_questions[topic][level].append(question_dict)

    return trivia_questions


# Handles selection and scrambling of 15-letter word or phrase
def scramble_letters():
    # Initialize empty dictionary to store 15-letter words/phrases and clues
    scramble_words = {}

    # Open the CSV file (and close automatically when with block exited)
    with open(f"csv/scramble_words.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        # For each row in the CSV file:
        for row in reader:
            # Extract 'word' and 'clue' and store in dictionary
            word = row["word"]
            clue = row["clue"]
            scramble_words[word] = clue

        # Select random 15-letter word/phrase with corresponding from dictionary
        selected_word = random.choice(list(scramble_words.keys()))
        scramble_clue = scramble_words[selected_word]

        # Convert selected_word into a list of characters
        selected_word_list = list(selected_word)

        # Create a copy of the original list
        original_word_list = selected_word_list.copy()

        # Shuffle the list of characters
        random.shuffle(selected_word_list)

        # While the shuffled list has any two adjacent characters that were adjacent in the original word:
        while check_adjacent(original_word_list, selected_word_list):
            # Shuffle the list of characters
            random.shuffle(selected_word_list)

        original_word = "".join(original_word_list)

        # Return scrambled list of letters and the clue for use in the main function
        return original_word, selected_word_list, scramble_clue


def check_adjacent(original, shuffled):
    for i in range(len(shuffled) - 2):
        for j in range(len(original) - 2):
            if (shuffled[i], shuffled[i + 1]) == (original[j], original[j + 1]):
                return True
    return False


# Handles logic for each round of the game.
def play_round(questions, category, score, letters_collected, scrambled_letters, asked_questions):
    # Index levels to scores
    level_scores = {"1": 1, "2": 2, "3": 3}

    while True:
        # Store levels available based on current score
        levels_available = [str(i) for i in range(1, min(4, 16 - score))]

        # Prompt player for desired difficulty level and reprompt if level not available
        difficulty = input(
            f"\nWelcome to room {score + 1}. Choose a door ({', '.join(levels_available)}): "
        )

        if difficulty in levels_available:
            break
        else:
            print(
                f"Invalid door. Choose from {', '.join(levels_available)}"
            )

    while True:
        # Retrieve questions of the chosen difficulty from the questions dictionary
        chosen_questions = questions[category][difficulty]

        # Filter out questions that have already been asked
        available_questions = [q for q in chosen_questions if q not in asked_questions]

        if not available_questions:
            print("This door seems to be sealed. Choose another door.")
            break

        # Randomly select a question of the chosen difficulty from the list of questions
        selected_question = random.choice(available_questions)

        # Add the selected question to the list of asked questions
        asked_questions.append(selected_question)

        # Store correct choice as string for comparison with player answer
        correct_choice_key = int(selected_question["correct_choice"]) - 1
        correct_choice = selected_question["choices"][correct_choice_key].lower()

        # Shuffle the order of the answers
        shuffled_choices = random.sample(
            selected_question["choices"], len(selected_question["choices"])
        )

        # Present the question and its multiple-choice answers to the player
        print(f"\n{selected_question['question']}")
        for choice in shuffled_choices:
            print(f"- {choice}")

        # Prompt the player for their answer
        player_choice = input("\nAnswer: ").lower()

        # If the player answers correctly:
        if player_choice == correct_choice:
            print("Correct!\n")

            # Pop letters from the scrambled word based on the difficulty level
            letters_to_pop = int(difficulty)
            popped_letters = []
            for _ in range(letters_to_pop):
                popped_letter = scrambled_letters.pop(0)
                popped_letters.append(popped_letter)

            # Display rewarded letters to player and add them to the letters_collected list
            if len(popped_letters) == 1:
                print(f"The door unlocks. On a table beyond the door, you find a tile inscribed with a letter: {''.join(popped_letters)}.\nYou place the tile in your bag and walk along the corridor to the next room.")
            else:
                print(f"The door unlocks. On a table beyond the door, you find some tiles inscribed with letters: {', '.join(popped_letters)}.\nYou place the tiles in your bag and walk along the corridor to the next room.")

            letters_collected.extend(popped_letters)

            # Increment score by the difficulty level
            score += level_scores[difficulty]
            break

        # If question answered incorrectly...
        else:
            print(
                "Incorrect. You'll have to try another door.\n"
            )

        while True:
            # Ask player to choose a new difficulty level from the remaining options
            new_levels_available = [
                lvl for lvl in levels_available if lvl != difficulty
            ]
            new_difficulty = input(
                f"Choose a different door ({', '.join(new_levels_available)}): "
            )
            if new_difficulty in new_levels_available:
                break
            else:
                print(
                    f"Invalid door. Choose from {', '.join(new_levels_available)}"
                )

    return score, letters_collected, scrambled_letters, asked_questions


# Handles final word scramble. Could take the collected letters as a parameter and return whether the player has won or lost.
def final_puzzle(original_word, scrambled_letters, scramble_clue):
    scrambled_word = ''.join(scrambled_letters)
    while True:
        confirm = input("\nYou come to the heavy door leading to the final room! Are you ready to enter? (y/n) ").lower()
        if confirm == "n":
            continue
        elif confirm == "y":
            print("\nIn the middle of the room, you see a table adorned with a row of 15 sunken squares.")
            print(f"\nThe squares seem to be sized to accommodate the set of tiles you have in your bag: {scrambled_word}")
            clue = input("\nAn envelope marked CLUE sits below the row of squares. Would you like to open it? (y/n) ")
            if clue == "y":
                print(f"CLUE: {scramble_clue}")
            elif clue != "n":
                print("Invalid input. Please enter 'y' or 'n'.")

            attempt = 0
            while attempt < 2:
                answer = input("Answer: ").replace(" ", "")

                if answer.lower() == original_word.lower():
                    return True
                else:
                    print("That's incorrect.")
                    attempt += 1
                    if attempt < 2:
                        clue = input("Would you like to look at the CLUE? (y/n) ")
                        if clue == "y":
                            print(f"CLUE: {scramble_clue}")
                    else:
                        break
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()

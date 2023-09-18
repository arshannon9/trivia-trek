# Copyright (C) 2023 Anthony Ryan Shannon/Ars Artis Softworks

import random
from unittest.mock import patch
from trivia_trek import (
    load_questions,
    scramble_letters,
    check_adjacent,
    play_round,
    final_puzzle,
)

# Mocking the random.choice function to ensure consistent behavior during testing
random.choice = lambda seq: seq[0]


# Call test functions
def main():
    test_load_questions()
    test_scramble_letters()
    test_check_adjacent()
    test_play_round_correct_answer()
    test_final_puzzle_correct_answer()


# Test function for loading questions
def test_load_questions():
    questions = load_questions("geography")
    assert len(questions) > 0, "No questions loaded."
    assert "geography" in questions, "Category not loaded."
    assert "1" in questions["geography"], "Difficulty level not loaded."
    assert "2" in questions["geography"], "Difficulty level not loaded."
    assert "3" in questions["geography"], "Difficulty level not loaded."


# Test function for scrambling letters
def test_scramble_letters():
    original_word, scrambled_letters, scramble_clue = scramble_letters()
    assert len(original_word) == 15, "Word not correct length."
    assert len(scrambled_letters) == 15, "Scrambled letters not correct length."
    assert scramble_clue.strip() != "", "Clue not loaded."
    assert original_word != "".join(scrambled_letters), "Letters not scrambled."


# Test function for checking adjacent letters in scrambled word
def test_check_adjacent():
    original = "original"
    shuffled = "irognail"
    assert check_adjacent(original, shuffled) == True, "Adjacent letters not detected."

    original = "example"
    shuffled = "xmleape"
    assert (
        check_adjacent(original, shuffled) == False
    ), "Adjacent letters detected incorrectly."


# Test function for playing a round, mocking user input with correct answer
def test_play_round_correct_answer():
    # Prepare mock question to answer
    mock_question = {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Rome"],
        "correct_choice": "1",
    }

    # Prepare mock input sequence for test
    input_sequence = [
        "1",  # Choose difficulty level
        "Paris",  # Input correct answer
    ]

    # Mock user input for test
    with patch("builtins.input", side_effect=input_sequence):
        score, letters_collected, scrambled_letters, asked_questions = play_round(
            {"geography": {"1": [mock_question]}},
            "geography",
            0,
            [],
            ["A"],
            [],
        )

    assert score == 1, "Score not updated correctly."
    assert len(letters_collected) == 1, "Letters collected when answered correctly."
    assert (
        len(scrambled_letters) == 0
    ), "Scrambled letters changed when answered correctly."
    assert len(asked_questions) == 1, "Question not added to asked_questions."
    assert (
        asked_questions[0] == mock_question
    ), "Question added to asked_questions incorrectly."


# Test function for solving the final puzzle, mocking user input with correct answer
def test_final_puzzle_correct_answer():
    original_word = "example"
    scrambled_letters = list("xmleape")
    scramble_clue = "A sample word."

    # Mock user input for solving the puzzle correctly on the first attempt
    with patch(
        "builtins.input", side_effect=["y", "n", "exlmaepa", "y", "example"]
    ):  # Simulate answering yes, no, entering correct answer, and answering yes to the clue
        result = final_puzzle(original_word, scrambled_letters, scramble_clue)

    assert result == True, "Final puzzle not solved correctly."


if __name__ == "__main__":
    main()

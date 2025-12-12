"""Hangman Game - Guess the word before you run out of tries!"""

import random


HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   \\|
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |    |
       |
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |    |
       |   / \\
    """
]

WORD_LIST = [
    "python", "hangman", "programming", "computer", "challenge",
    "developer", "algorithm", "database", "function", "variable",
    "beautiful", "fantastic", "adventure", "mysterious", "incredible"
]


def get_word():
    """Return a random word from the word list."""
    return random.choice(WORD_LIST).upper()


def display_hangman(tries):
    """Display the hangman ASCII art."""
    return HANGMAN_STAGES[len(HANGMAN_STAGES) - tries - 1]


def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def play_hangman():
    """Play a single game of Hangman."""
    word = get_word()
    guessed_letters = set()
    wrong_guesses = set()
    tries = 6
    won = False

    print("\n🎮 Welcome to HANGMAN!")
    print(f"The word has {len(word)} letters.\n")

    while tries > 0 and not won:
        print(display_hangman(tries))
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
        print(f"Tries left: {tries}\n")

        guess = input("Guess a letter: ").upper().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter!")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("⚠️  You already guessed that letter!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            tries -= 1
            print(f"❌ Sorry! '{guess}' is not in the word.")

        # Check if player won
        if all(letter in guessed_letters for letter in word):
            won = True

    print(display_hangman(tries))

    if won:
        print(f"\n🎉 YOU WON! The word was: {word}")
        return True
    else:
        print(f"\n😢 GAME OVER! The word was: {word}")
        return False


def main():
    """Main game loop."""
    wins = 0
    total = 0
    play_again = True

    while play_again:
        if play_hangman():
            wins += 1
        total += 1

        print(f"\n📊 Score: {wins}/{total}")
        response = input("Play again? (yes/no): ").lower()
        play_again = response in ("yes", "y")

    print(f"\n🏆 Final Score: {wins}/{total} wins. Thanks for playing!")


if __name__ == "__main__":
    main()

"""Guess the Number Game - Try to guess the secret number!"""

import random


def play_game(max_num=100, max_tries=7):
    """Play a single round of guessing game."""
    secret = random.randint(1, max_num)
    tries = 0
    guessed = False

    print(f"\n🎮 Welcome to Guess the Number!")
    print(f"I'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_tries} tries to guess it.\n")

    while tries < max_tries and not guessed:
        try:
            guess = int(input(f"Attempt {tries + 1}/{max_tries} - Enter your guess: "))
            tries += 1

            if guess < 1 or guess > max_num:
                print(f"Please enter a number between 1 and {max_num}!")
                tries -= 1
                continue

            if guess == secret:
                print(f"\n🎉 Correct! The number was {secret}!")
                print(f"You got it in {tries} tries!")
                guessed = True
            elif guess < secret:
                diff = secret - guess
                hint = "much higher" if diff > 20 else "higher"
                print(f"❌ Too low! Try {hint}. ({diff} away)")
            else:
                diff = guess - secret
                hint = "much lower" if diff > 20 else "lower"
                print(f"❌ Too high! Try {hint}. ({diff} away)")

        except ValueError:
            print("⚠️  Please enter a valid number!")
            tries -= 1

    if not guessed:
        print(f"\n😢 Game Over! The number was {secret}.")
        print("Better luck next time!")

    return guessed, tries


def main():
    play_again = True
    wins = 0
    total = 0

    while play_again:
        won, attempts = play_game()
        total += 1
        if won:
            wins += 1

        print(f"\nStats: {wins} wins out of {total} games")
        response = input("Play again? (yes/no): ").lower()
        play_again = response in ("yes", "y")

    print(f"\n📊 Final Score: {wins}/{total} wins. Thanks for playing!")


if __name__ == "__main__":
    main()

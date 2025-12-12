"""Rock Paper Scissors Game - Beat the Computer!"""

import random


def get_computer_choice():
    """Return random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player, computer):
    """Determine winner between player and computer."""
    if player == computer:
        return "tie"
    
    winning_combos = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combos[player] == computer:
        return "player"
    return "computer"


def display_result(player, computer, result):
    """Display the result of a round."""
    print(f"\n{'='*40}")
    print(f"You chose:     {player.upper()}")
    print(f"Computer chose: {computer.upper()}")
    print(f"{'='*40}")
    
    if result == "tie":
        print("🤝 It's a TIE!")
    elif result == "player":
        print("🎉 YOU WIN this round!")
    else:
        print("🤖 COMPUTER WINS this round!")


def play_round():
    """Play a single round of rock-paper-scissors."""
    valid_choices = ["rock", "paper", "scissors"]
    
    while True:
        player_input = input("\nRock, Paper, or Scissors? (or 'quit' to exit): ").lower().strip()
        
        if player_input == "quit":
            return None
        
        if player_input not in valid_choices:
            print("⚠️  Invalid choice! Try 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(player_input, computer_choice)
        display_result(player_input, computer_choice, result)
        
        return result


def main():
    """Main game loop."""
    print("\n🎮 Welcome to Rock Paper Scissors!")
    print("First to 3 wins takes the match!\n")
    
    player_wins = 0
    computer_wins = 0
    
    while player_wins < 3 and computer_wins < 3:
        result = play_round()
        
        if result is None:
            break
        
        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
        
        print(f"\n📊 Score: You {player_wins} - Computer {computer_wins}")
    
    print(f"\n{'='*40}")
    if player_wins == 3:
        print("🏆 YOU WON THE MATCH! Congratulations!")
    elif computer_wins == 3:
        print("🤖 COMPUTER WON THE MATCH! Better luck next time!")
    else:
        print("Game ended. Thanks for playing!")
    print(f"{'='*40}\n")


if __name__ == "__main__":
    main()

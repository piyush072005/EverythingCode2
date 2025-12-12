"""2048 Game - Slide tiles to combine numbers and reach 2048!"""

import random
import os


class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        """Add a new tile (2 or 4) to a random empty position."""
        empty_positions = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_positions:
            i, j = random.choice(empty_positions)
            self.board[i][j] = random.choice([2, 2, 2, 4])  # 75% chance for 2, 25% for 4

    def display(self):
        """Display the game board."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n🎮 2048 GAME")
        print(f"Score: {self.score}\n")
        
        for row in self.board:
            print("┌─────┬─────┬─────┬─────┐")
            print("│" + "│".join(f"{num:>4} " for num in row) + "│")
        print("└─────┴─────┴─────┴─────┘\n")
        print("Controls: 'a' (left), 'd' (right), 'w' (up), 's' (down), 'q' (quit)")

    def move_left(self):
        """Slide tiles to the left."""
        changed = False
        for i in range(4):
            # Remove zeros
            non_zero = [val for val in self.board[i] if val != 0]
            # Merge tiles
            merged = []
            j = 0
            while j < len(non_zero):
                if j + 1 < len(non_zero) and non_zero[j] == non_zero[j + 1]:
                    merged.append(non_zero[j] * 2)
                    self.score += non_zero[j] * 2
                    j += 2
                else:
                    merged.append(non_zero[j])
                    j += 1
            # Pad with zeros
            merged += [0] * (4 - len(merged))
            if merged != self.board[i]:
                changed = True
            self.board[i] = merged
        return changed

    def move_right(self):
        """Slide tiles to the right."""
        for i in range(4):
            self.board[i].reverse()
        changed = self.move_left()
        for i in range(4):
            self.board[i].reverse()
        return changed

    def move_up(self):
        """Slide tiles upward."""
        # Transpose
        self.board = [list(row) for row in zip(*self.board)]
        changed = self.move_left()
        # Transpose back
        self.board = [list(row) for row in zip(*self.board)]
        return changed

    def move_down(self):
        """Slide tiles downward."""
        # Transpose
        self.board = [list(row) for row in zip(*self.board)]
        for i in range(4):
            self.board[i].reverse()
        changed = self.move_left()
        for i in range(4):
            self.board[i].reverse()
        # Transpose back
        self.board = [list(row) for row in zip(*self.board)]
        return changed

    def is_game_over(self):
        """Check if there are no valid moves left."""
        # Check for empty cells
        for row in self.board:
            if 0 in row:
                return False
        # Check for possible merges
        for i in range(4):
            for j in range(4):
                current = self.board[i][j]
                if j + 1 < 4 and current == self.board[i][j + 1]:
                    return False
                if i + 1 < 4 and current == self.board[i + 1][j]:
                    return False
        return True

    def has_won(self):
        """Check if the player has reached 2048."""
        return any(2048 in row for row in self.board)

    def play(self):
        """Main game loop."""
        won = False

        while True:
            self.display()

            if self.has_won() and not won:
                print("🎉 YOU REACHED 2048! (Continue playing or press 'q' to quit)")
                won = True

            if self.is_game_over():
                print("😢 GAME OVER! No more moves available.")
                print(f"Final Score: {self.score}\n")
                break

            move = input("Enter move: ").lower().strip()

            if move == 'q':
                print(f"Thanks for playing! Final Score: {self.score}\n")
                break
            elif move == 'a':
                if self.move_left():
                    self.add_new_tile()
            elif move == 'd':
                if self.move_right():
                    self.add_new_tile()
            elif move == 'w':
                if self.move_up():
                    self.add_new_tile()
            elif move == 's':
                if self.move_down():
                    self.add_new_tile()
            else:
                print("⚠️  Invalid move! Use 'a', 'd', 'w', 's', or 'q'.")


def main():
    game = Game2048()
    game.play()


if __name__ == "__main__":
    main()

from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")

        while True:
            self.board.print()

            if self.turn == "X":
                raw = input("Column (1-7), or q: ").strip().lower()

                if raw == "q":
                    print("Game ended.")
                    return

                try:
                    col = int(raw) - 1
                except ValueError:
                    print("Invalid input. Enter a column number.")
                    continue

            else:
                col = self.ai.choose_column(self.board)

            # Attempt to place the disc.
            row = (
                self.board.drop(col, self.turn)
                if col is not None
                else None
            )

            # Handle invalid moves and unavailable columns.
            if row is None:
                print("Column unavailable. Choose another column.")

                if self.turn == "O":
                    print("Game ended.")
                    return

                continue

            # Give feedback once for each successful move.
            print(f"{self.turn} placed a disc in column {col + 1}.")

            # Check for a winner before requesting another move.
            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return

            # Check for a draw.
            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            # Switch turns only when the game continues.
            self.turn = "O" if self.turn == "X" else "X"
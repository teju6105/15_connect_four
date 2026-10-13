import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        # Find all columns where a disc can legally be placed.
        legal = [
            c for c in range(7)
            if board.grid[0][c] == "."
        ]

        # No legal moves remain.
        if not legal:
            return None

        # 1. Take an immediate winning move.
        for col in legal:
            row = board.drop(col, me)

            if board.winner(me):
                board.grid[row][col] = "."
                return col

            # Undo the simulated move.
            board.grid[row][col] = "."

        # 2. Block an immediate opponent win.
        for col in legal:
            row = board.drop(col, opponent)

            opponent_can_win = board.winner(opponent)

            # Undo the simulated move.
            board.grid[row][col] = "."

            if opponent_can_win:
                return col

        # 3. No immediate win or block is required.
        return random.choice(legal)

import time
from typing import List, Optional, Tuple


class Player:
    
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color  # "B" for Black, "R" for Red
        self.moves_count = 0
        self.result = "Ongoing"  # Win, Loss, Draw, Quit
        self.start_time = time.time()
        self.elapsed_time = 0.0

    def finalize_time(self):
        self.elapsed_time = time.time() - self.start_time

class Checker:
    "To store information about each checker"

    def __init__(self, color: str, row: int, col: int):
        self.color = color  # "B" or "R"
        self.row = row
        self.col = col
        self.is_king = False

    def promote(self):
        "To promote a standard checker to a King."
        self.is_king = True

    def move_to(self, new_row: int, new_col: int):
        "Update the position of the checker"
        self.row = new_row
        self.col = new_col
        # Check automatic promotion conditions
        if self.color == "B" and self.row == 7:
            self.promote()
        elif self.color == "R" and self.row == 0:
            self.promote()

class Board:
    "This class contains the current status of the game and manages the array of checkers"

    def __init__(self):
        self.grid_size = 8
        self.checkers: List[Checker] = []
        self.setup_board()

    def setup_board(self):
        "Initializes standard 8x8 Checkers layout (Black at top, Red at bottom)"
        self.checkers.clear()
        # Setup Black pieces (rows 0-2)
        for row in range(3):
            for col in range(self.grid_size):
                if (row + col) % 2 == 1:
                    self.checkers.append(Checker("B", row, col))

        # Setup Red pieces (rows 5-7)
        for row in range(5, 8):
            for col in range(self.grid_size):
                if (row + col) % 2 == 1:
                    self.checkers.append(Checker("R", row, col))

    def get_piece_at(self, row: int, col: int) -> Optional[Checker]:
        "Returns the checker piece at a given coordinate, or None if empty"
        for piece in self.checkers:
            if piece.row == row and piece.col == col:
                return piece
        return None

    def display(self):
        "Renders the current status of the board in the terminal"
        print("\n    0   1   2   3   4   5   6   7  ")
        print("  +---+---+---+---+---+---+---+---+")
        for r in range(self.grid_size):
            row_str = f"{r} |"
            for c in range(self.grid_size):
                piece = self.get_piece_at(r, c)
                if piece:
                    symbol = " B " if piece.color == "B" else " R "
                    if piece.is_king:
                        symbol = symbol.lower().replace(" ", "K")  # bK or rK
                    row_str += symbol + "|"
                else:
                    # Mark dark squares vs light squares
                    if (r + c) % 2 == 1:
                        row_str += "   |"
                    else:
                        row_str += " # |"
            print(row_str)
            print("  +---+---+---+---+---+---+---+---+")
        print("Legend: B = Black, R = Red (Lowercase 'k' denotes King)\n")

    def is_valid_move(self, piece: Checker, target_row: int, target_col: int) -> Tuple[bool, Optional[Checker]]:
        " Validates if a move or jump is legal. Returns (is_valid, jumped_piece)"
        # Target must be within bounds and on a dark square
        if not (0 <= target_row < self.grid_size and 0 <= target_col < self.grid_size):
            return False, None
        if (target_row + target_col) % 2 != 1:
            return False, None

        # Target cell must be empty
        if self.get_piece_at(target_row, target_col) is not None:
            return False, None

        row_diff = target_row - piece.row
        col_diff = target_col - abs(target_col - piece.col) # relative column step magnitude
        col_step = target_col - piece.col

        # Determine allowed movement direction
        valid_forward = False
        if piece.color == "B" and row_diff > 0:
            valid_forward = True
        elif piece.color == "R" and row_diff < 0:
            valid_forward = True

        is_king_move = piece.is_king and abs(row_diff) == 1 and abs(col_step) == 1
        is_regular_move = valid_forward and abs(row_diff) == 1 and abs(col_step) == 1

        # Simple 1-step move
        if is_king_move or is_regular_move:
            return True, None

        # Check for Jump / Capture (2 steps diagonal)
        is_king_jump = piece.is_king and abs(row_diff) == 2 and abs(col_step) == 2
        is_regular_jump = valid_forward and abs(row_diff) == 2 and abs(col_step) == 2

        if is_king_jump or is_regular_jump:
            mid_row = (piece.row + target_row) // 2
            mid_col = (piece.col + target_col) // 2
            middle_piece = self.get_piece_at(mid_row, mid_col)

            if middle_piece and middle_piece.color != piece.color:
                return True, middle_piece

        return False, None

    def execute_move(self, piece: Checker, target_row: int, target_col: int) -> bool:
        """Executes a validated move, handles capturing, and updates the board."""
        valid, jumped_piece = self.is_valid_move(piece, target_row, target_col)
        if not valid:
            return False

        piece.move_to(target_row, target_col)

        if jumped_piece:
            self.checkers.remove(jumped_piece)

        return True


class Game:
    """Controls the overall game loop, player turn management, and game summary."""

    def __init__(self, player1_name: str, player2_name: str):
        self.player1 = Player(player1_name, "B")  # Black goes first
        self.player2 = Player(player2_name, "R")
        self.board = Board()
        self.current_player = self.player1

    def switch_turn(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def check_win_condition(self) -> Optional[Player]:
        """Checks if one player has lost all pieces."""
        black_pieces = [p for p in self.board.checkers if p.color == "B"]
        red_pieces = [p for p in self.board.checkers if p.color == "R"]

        if not black_pieces:
            return self.player2
        if not red_pieces:
            return self.player1
        return None

    def play(self):
        """Main game loop handling turns, player prompts, and statistics summary."""
        print("=== WELCOME TO PYTHON CHECKERS ===")
        
        while True:
            self.board.display()
            winner = self.check_win_condition()
            if winner:
                print(f"*** Game Over! {winner.name} wins by eliminating all opposing checkers! ***")
                winner.result = "Win"
                loser = self.player2 if winner == self.player1 else self.player1
                loser.result = "Loss"
                break

            print(f"Current Turn: {self.current_player.name} ({'Black (B)' if self.current_player.color == 'B' else 'Red (R)'})")
            choice = input("Enter [m] to Move or [f] to Finish/Quit game: ").strip().lower()

            if choice == 'f':
                print(f"\n{self.current_player.name} chose to finish/quit the game.")
                self.current_player.result = "Quit (Loss)"
                other_player = self.player2 if self.current_player == self.player1 else self.player1
                other_player.result = "Win (Default)"
                break
            elif choice == 'm':
                try:
                    print("Enter source position:")
                    sr = int(input("  Source Row (0-7): "))
                    sc = int(input("  Source Col (0-7): "))
                    
                    piece = self.board.get_piece_at(sr, sc)
                    if not piece or piece.color != self.current_player.color:
                        print("❌ Invalid selection. You must select your own piece.")
                        continue

                    print("Enter target position:")
                    tr = int(input("  Target Row (0-7): "))
                    tc = int(input("  Target Col (0-7): "))

                    success = self.board.execute_move(piece, tr, tc)
                    if success:
                        self.current_player.moves_count += 1
                        print("✅ Move successful!")
                        self.switch_turn()
                    else:
                        print("❌ Invalid move rule violation. Try again.")
                except ValueError:
                    print("❌ Please enter valid integer coordinates between 0 and 7.")
            else:
                print("❌ Invalid choice. Please enter 'm' or 'f'.")

        # Finalize stats
        self.player1.finalize_time()
        self.player2.finalize_time()
        self.show_summary()

    def show_summary(self):
        """Summarizes and displays general game statistics."""
        print("\n" + "="*40)
        print("           GAME SUMMARY REPORT          ")
        print("="*40)
        for p in [self.player1, self.player2]:
            print(f"Player Name : {p.name}")
            print(f"Piece Color : {'Black' if p.color == 'B' else 'Red'}")
            print(f"Total Moves : {p.moves_count}")
            print(f"Game Result : {p.result}")
            print(f"Time Played : {p.elapsed_time:.2f} seconds")
            print("-" * 40)

if __name__ == "__main__":
    p1 = input("Enter name for Player 1 (Black pieces): ") or "Player 1"
    p2 = input("Enter name for Player 2 (Red pieces): ") or "Player 2"
    
    game = Game(p1, p2)
    game.play()
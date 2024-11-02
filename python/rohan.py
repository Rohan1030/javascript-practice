class ChessPiece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'R')

class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'N')

class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'B')

class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'Q')

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'K')

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'P')

class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Set up pawns
        for i in range(8):
            self.board[1][i] = Pawn('white')
            self.board[6][i] = Pawn('black')

        # Set up other pieces
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_class in enumerate(piece_order):
            self.board[0][i] = piece_class('white')
            self.board[7][i] = piece_class('black')

    def display(self):
        for row in range(7, -1, -1):
            print(f"{row + 1} ", end="")
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    print(f"{piece.color[0]}{piece.symbol}", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("  a b c d e f g h")

    def move_piece(self, from_pos, to_pos):
        from_col, from_row = ord(from_pos[0]) - ord('a'), int(from_pos[1]) - 1
        to_col, to_row = ord(to_pos[0]) - ord('a'), int(to_pos[1]) - 1

        piece = self.board[from_row][from_col]
        if piece is None:
            return False

        # Basic move validation (does not include chess rules)
        if 0 <= to_row < 8 and 0 <= to_col < 8:
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = None
            return True
        return False

def main():
    board = ChessBoard()
    print("Welcome to Python Chess!")
    print("Enter moves in the format 'e2 e4'")
    print("Type 'quit' to end the game.")

    while True:
        board.display()
        move = input("Enter your move: ")
        
        if move.lower() == 'quit':
            break

        try:
            from_pos, to_pos = move.split()
            if board.move_piece(from_pos, to_pos):
                print("Move successful!")
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Use format 'e2 e4'.")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
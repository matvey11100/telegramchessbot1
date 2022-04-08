from ChessPiece import ChessPiece
from Bishop import Bishop
from Rock import Rock


class Queen(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = "Q"

    def possible_moves(self, board, p0, p1):
        moves = []
        # Ферзь объединяет в себе слона и ладью, можно просто сложить их возможные ходы
        moves.extend(Bishop.possible_moves(Bishop(self.colour), board, p0, p1))
        moves.extend(Rock.possible_moves(Rock(self.colour), board, p0, p1))
        return moves

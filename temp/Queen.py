from ChessPiece import ChessPiece
from Bishop import Bishop
from Rook import Rook
import copy


class Queen(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = "Q"

    def possible_moves(self, board, p0, p1):
        moves = self.possible_moves_2(board, p0, p1)
        moves_2 = copy.deepcopy(moves)
        for i, j in moves_2:
            if board.will_be_no_check(p0, p1, i, j):
                pass
            else:
                moves.remove([i, j])
        return moves

    def possible_moves_2(self, board, p0, p1):
        moves = []
        # Ферзь объединяет в себе слона и ладью, можно просто сложить их возможные ходы
        moves.extend(Bishop.possible_moves_2(Bishop(self.colour), board, p0, p1))
        moves.extend(Rook.possible_moves_2(Rook(self.colour), board, p0, p1))
        return moves
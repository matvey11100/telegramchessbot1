from ChessPiece import ChessPiece
import copy


class Knight(ChessPiece):

    def __init__(self, colour):
        super().__init__(colour)
        self.name = "N"


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
        combinations = [
            [p0 + 2, p1 + 1], [p0 + 2, p1 - 1],
            [p0 - 2, p1 + 1], [p0 - 2, p1 - 1],
            [p0 + 1, p1 - 2], [p0 - 1, p1 - 2],
            [p0 + 1, p1 + 2], [p0 - 1, p1 + 2]
        ]
        for i, j in combinations:
            if board.is_empty(i, j) or board.contains_an_enemy(i, j, self.enemy_colour):
                moves.append([i, j])
        return moves
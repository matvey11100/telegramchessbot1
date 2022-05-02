from ChessPiece import ChessPiece
import copy

class Bishop(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = "B"

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
        p0_ = p0
        p1_ = p1
        while True:
            p0_ += 1
            p1_ += 1
            if board.is_empty(p0_, p1_) or board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                b2 = board.board
                moves.append([p0_, p1_])
                if board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                    break
            else:
                break
        p0_ = p0
        p1_ = p1
        while True:
            p0_ -= 1
            p1_ += 1
            if board.is_empty(p0_, p1_) or board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                moves.append([p0_, p1_])
                if board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                    break
            else:
                break
        p0_ = p0
        p1_ = p1
        while True:
            p0_ += 1
            p1_ -= 1
            if board.is_empty(p0_, p1_) or board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                moves.append([p0_, p1_])
                if board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                    break
            else:
                break
        p0_ = p0
        p1_ = p1
        while True:
            p0_ -= 1
            p1_ -= 1
            if board.is_empty(p0_, p1_) or board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                moves.append([p0_, p1_])
                if board.contains_an_enemy(p0_, p1_, self.enemy_colour):
                    break
            else:
                break

        return moves
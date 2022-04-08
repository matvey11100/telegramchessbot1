from ChessPiece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = "B"

    def possible_moves(self, board, p0, p1):
        moves = []
        p0_ = p0
        p1_ = p1
        while True:
            p0_ += 1
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

from ChessPiece import ChessPiece


class Rock(ChessPiece):
    castling = True  # Пока ладья не походила, рокировка в ее сторону доступна

    def __init__(self, colour, castling):
        super().__init__(colour)
        self.name = "R"
        self.castling = castling

    def possible_moves(self, board, p0, p1):
        moves = []
        p0_ = p0
        p1_ = p1
        while True:
            p0_ += 1
            if board.is_empty(p0_, p1) or board.contains_an_enemy(p0_, p1, self.enemy_colour):
                moves.append([p0_, p1])
                if board.contains_an_enemy(p0_, p1, self.enemy_colour):
                    break
            else:
                break
        p0_ = p0
        p1_ = p1
        while True:
            p0_ -= 1
            if board.is_empty(p0_, p1) or board.contains_an_enemy(p0_, p1, self.enemy_colour):
                moves.append([p0_, p1])
                if board.contains_an_enemy(p0_, p1, self.enemy_colour):
                    break
            else:
                break
        p0_ = p0
        p1_ = p1
        while True:
            p1_ += 1
            if board.is_empty(p0, p1_) or board.contains_an_enemy(p0, p1_, self.enemy_colour):
                moves.append([p0, p1_])
                if board.contains_an_enemy(p0, p1_, self.enemy_colour):
                    break
            else:
                break
        p0_ = p0
        p1_ = p1
        while True:
            p1_ -= 1
            if board.is_empty(p0, p1_) or board.contains_an_enemy(p0, p1_, self.enemy_colour):
                moves.append([p0, p1_])
                if board.contains_an_enemy(p0, p1_, self.enemy_colour):
                    break
            else:
                break
        return moves
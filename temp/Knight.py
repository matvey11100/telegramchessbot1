from ChessPiece import ChessPiece


class Knight(ChessPiece):

    def __init__(self, colour, castling):
        super().__init__(colour)
        self.name = "N"
        self.castling = castling

    def possible_moves(self, board, p0, p1):
        moves = []
        combinations = [
            [p0+2, p1+1], [p0+2, p1-1],
            [p0-2, p1+1], [p0-2, p1-1],
            [p0+1, p1-2], [p0-1, p1-2],
            [p0+1, p1+2], [p0-1, p1+2]
        ]
        for i, j in combinations:
            if board.is_empty(i, j) or board.contains_an_enemy(i, j, self.enemy_colour):
                moves.append([i, j])
        return moves

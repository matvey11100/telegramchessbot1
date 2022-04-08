from ChessPiece import ChessPiece


class King(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = "K"

    def possible_moves(self, board, p0, p1):
        moves = []
        combinations = [[p0+1, p1+1], [p0+1, p1+0],
                        [p0+1, p1-1], [p0-1, p1+1],
                        [p0-1, p1-1], [p0-1, p1+0],
                        [p0+0, p1+1], [p0+0, p1-1]
                        ]
        for i, j in combinations:
            if board.is_empty(i, j) or board.contains_an_enemy(i, j, self.enemy_colour):
                # Нужно проверить, не попадает ли в этой клетке король под шах
                if self.check_for_check(board, i, j):
                    moves.append([i, j])

        return moves

    def possible_moves_2(self, board, p0, p1):
        moves = []
        combinations = [[p0 + 1, p1 + 1], [p0 + 1, p1 + 0],
                        [p0 + 1, p1 - 1], [p0 - 1, p1 + 1],
                        [p0 - 1, p1 - 1], [p0 - 1, p1 + 0],
                        [p0 + 0, p1 + 1], [p0 + 0, p1 - 1]
                        ]
        for i, j in combinations:
            if board.is_empty(i, j) or board.contains_an_enemy(i, j, self.enemy_colour):
                moves.append([i, j])
        return moves

    def check_for_check(self, board, i, j):
        for a in range(8):
            for b in range(8):
                figure = board.board[a][b]
                if figure.colour == self.enemy_colour:
                    if [i, j] in figure.possible_moves_2(board, a, b):
                        return False
        return True
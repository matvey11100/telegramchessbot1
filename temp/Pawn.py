from ChessPiece import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, colour):
        super().__init__(colour)
        self.name = "p"

    def possible_moves(self, board, p0, p1):
        moves = []

        if self.colour == "white":
            if [p0, p1] in board.take_on_the_pass:
                moves.append([p0 - 1, board.take_on_the_pass[0]])
            if p0 == 6:
                if board.is_empty(5, p1):
                    moves.append([5, p1])
                    if board.is_empty(4, p1):
                        moves.append([4, p1])
            else:
                if board.is_empty(p0 - 1, p1):
                    moves.append([p0 - 1, p1])
            if board.contains_an_enemy(p0 - 1, p1 + 1, self.enemy_colour):
                moves.append([p0 - 1, p1 + 1])
            if board.contains_an_enemy(p0 - 1, p1 - 1, self.enemy_colour):
                moves.append([p0 - 1, p1 - 1])
        else:
            if [p0, p1] in board.take_on_the_pass:
                moves.append([p0 + 1, board.take_on_the_pass[0]])
            if p0 == 1:
                if board.is_empty(2, p1):
                    moves.append([2, p1])
                    if board.is_empty(3, p1):
                        moves.append([3, p1])
            else:
                if board.is_empty(p0 + 1, p1):
                    moves.append([p0 + 1, p1])
            if board.contains_an_enemy(p0 + 1, p1 + 1, self.enemy_colour):
                moves.append([p0 + 1, p1 + 1])
            if board.contains_an_enemy(p0 + 1, p1 - 1, self.enemy_colour):
                moves.append([p0 + 1, p1 - 1])


        return moves

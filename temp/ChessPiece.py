class ChessPiece:
    """
    Базовый класс шахматной фигуры
    """
    def __init__(self, colour):
        self.name = "0"  # имя "0" свидетельствует о пустой клетке
        self.colour = colour
        self.castling = False
        if colour == "white":
            self.enemy_colour = "black"
        else:
            self.enemy_colour = "white"


    def possible_moves(self, board, p0, p1):
        return False

    def possible_moves_2(self, board, p0, p1):
        # Для избежания рекурсии, когда 2 короля находятся рядом
        return self.possible_moves(board, p0, p1)
from ChessPiece import ChessPiece
from Pawn import Pawn
from King import King
from Rock import Rock
from Bishop import Bishop
from Queen import Queen
from Knight import Knight


class Board:

    board = []

    take_on_the_pass = []  # Ситуация с возможностью взятия на проходе


    def __init__(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                piece = ChessPiece("None")
                self.board[i].append(piece)

    def make_a_starting_position(self):  # Расставляем фигуры в стартовую позицию
        # расставляем пешки
        for i in range(8):
            self.board[1][i] = Pawn("black")
            self.board[6][i] = Pawn("white")
        # Короли
        self.board[0][4] = King("black")
        self.board[7][4] = King("white")
        # Ладьи
        self.board[0][0] = Rock("black")
        self.board[0][7] = Rock("black")
        self.board[7][0] = Rock("white")
        self.board[7][7] = Rock("white")
        # Кони
        self.board[0][1] = Knight("black")
        self.board[0][6] = Knight("black")
        self.board[7][1] = Knight("white")
        self.board[7][6] = Knight("white")
        # Слоны
        self.board[0][2] = Bishop("black")
        self.board[0][5] = Bishop("black")
        self.board[7][2] = Bishop("white")
        self.board[7][5] = Bishop("white")
        # Ферзи
        self.board[0][3] = Queen("black")
        self.board[7][3] = Queen("white")

    def is_empty(self, coord1, coord2):
        if coord1 < 0 or coord1 > 7 or coord2 < 0 or coord2 > 7:
            # Выходящие за пределы поля клетки считаем занятыми, чтобы туда было невозможно походить
            return False
        if self.board[coord1][coord2].name != "0":
            return False
        return True

    def contains_an_enemy(self, coord1, coord2, enemy_colour):
        if coord1 < 0 or coord1 > 7 or coord2 < 0 or coord2 > 7:
            # аналогично функции is_empty
            return False

        if self.board[coord1][coord2].colour != enemy_colour:
            return False
        return True

    def move(self, coord1, coord2, coord3, coord4):
        # Если взятие на проходе
        if len(self.take_on_the_pass):
            if [coord1, coord2] in self.take_on_the_pass and coord4 == self.take_on_the_pass[0]:
                self.board[coord3][coord4] = self.board[coord1][coord2]
                self.board[coord1][coord2] = ChessPiece("None")
                self.board[coord1][self.take_on_the_pass[0]] = ChessPiece("None")
                self.board[coord3][coord4].position = [coord3, coord4]
                return
        # Обычный ход
        self.board[coord3][coord4] = self.board[coord1][coord2]  # Переставляем фигуру
        self.board[coord1][coord2] = ChessPiece("None")  # Удаляем фигуру с прошлого места
        self.board[coord3][coord4].position = [coord3, coord4]  # Меняем в информации о фигуре ее координаты

        self.take_on_the_pass = []
        # Если походила пешка, то проверяем на возможность взять на проходе
        if self.board[coord3][coord4].name == "p" and abs(coord1 - coord3) == 2:
            self.take_on_the_pass_check(coord3, coord4)

    def take_on_the_pass_check(self, coord1, coord2):
        neighbours = coord2 + 1, coord2 - 1
        self.take_on_the_pass.append(coord2)
        for a in neighbours:
            if 0 <= a <= 7:
                if self.board[coord1][a].name == "p":
                    if self.board[coord1][a].colour != self.board[coord1][coord2].colour:
                        self.take_on_the_pass.append([coord1, a])
        if len(self.take_on_the_pass) == 1:
            self.take_on_the_pass = []

if __name__ == "__main__":
    b = Board()
    b.make_a_starting_position()

    for i in range(8):
        for j in range(8):
            print(b.board[i][j].name, b.board[i][j].colour, end="; ")
        print()

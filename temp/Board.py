from ChessPiece import ChessPiece
from Pawn import Pawn
from King import King
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from Knight import Knight
import copy

class Board:

    board = []

    colour = 'white' # Чей сейчас ход

    take_on_the_pass = []  # Ситуация с возможностью взятия на проходе

    def __init__(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                piece = ChessPiece("0")
                self.board[i].append(piece)

    def __getitem__(self, key):
        return self.board[key]

    def cout(self, bo):
        for i in range(8):
            for j in range(8):
                s = bo[i][j].name + " " + bo[i][j].colour
                print(f"{s:>8}", end="; ")
            print()

    def add(self, coord1, coord2, piece):
        self.board[coord1][coord2] = piece

    def make_a_starting_position(self):  # Расставляем фигуры в стартовую позицию
        # расставляем пешки
        for i in range(8):
            self.add(1, i, Pawn("black"))
            #self.board[1][i] = Pawn("black")
            self.board[6][i] = Pawn("white")
        # Короли
        self.board[0][4] = King("black")
        self.board[7][4] = King("white")
        # Ладьи
        self.board[0][0] = Rook("black")
        self.board[0][7] = Rook("black")
        self.board[7][0] = Rook("white")
        self.board[7][7] = Rook("white")
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

    def is_check(self, king_colour):
        # Определяем координаты короля
        coord1, coord2 = -1, -1
        for i in range(8):
            for j in range(8):
                if self.board[i][j].name == "K" and self.board[i][j].colour == king_colour:
                    coord1, coord2 = i, j
                    break
        if (coord1, coord2) == (-1, -1):
            return False
        for i in range(8):
            for j in range(8):
                if self.board[i][j].name != "0":
                    p = self.board[i][j]
                    if p.enemy_colour == king_colour and p.name != "K":
                        if [coord1, coord2] in p.possible_moves_2(self, i, j):
                            return True
                    elif p.enemy_colour == king_colour and p.name == "K":
                        if abs(coord1 - i) <= 1 >= abs(coord2 - j):
                            return True
        return False

    def will_be_no_check(self, c1, c2, c3, c4):
        """
        Когда мы ищем возможные ходы для фигуры, используем эту функцию чтобы проверить,
        не подставляется ли игрок под шах этим ходом
        """
        no_check = True
        board_copy = copy.deepcopy(self.board)
        self.move(c1, c2, c3, c4) # Моделируем позицию после хода
        if self.is_check(self.board[c3][c4].colour):
            # если подставляемся под шах, ход не подходит
            no_check = False
        self.board = copy.deepcopy(board_copy) # Возвращаем исходную позицию
        del board_copy
        return no_check

    def move(self, coord1, coord2, coord3, coord4):



        # Если взятие на проходе
        if len(self.take_on_the_pass):
            if [coord1, coord2] in self.take_on_the_pass and coord4 == self.take_on_the_pass[0]:
                self.board[coord3][coord4] = self.board[coord1][coord2]
                self.board[coord1][coord2] = ChessPiece("0")
                self.board[coord1][self.take_on_the_pass[0]] = ChessPiece("0")
                self.board[coord3][coord4].position = [coord3, coord4]
                return
        # Обычный ход
        self.board[coord3][coord4] = copy.deepcopy(self.board[coord1][coord2])  # Переставляем фигуру
        self.board[coord1][coord2] = ChessPiece("0")  # Удаляем фигуру с прошлого места

        self.take_on_the_pass = []
        # Если походила пешка, то проверяем на возможность взять на проходе
        if self.board[coord3][coord4].name == "p" and abs(coord1 - coord3) == 2:
            self.take_on_the_pass = [coord3, coord4]

        # Меняем очередность хода
        if self.colour == "white":
            self.colour = "black"
        else:
            self.colour = "white"

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

    def all_possible_moves(self, colour):
        list = {
            "p": {},
            "R": {},
            "N": {},
            "B": {},
            "Q": {},
            "K": {}
                }
        for i in range(8):
            for j in range(8):
                if self.board[i][j].colour == colour:
                    list[self.board[i][j].name][(i, j)] = self.board[i][j].possible_moves(self, i, j)
        l = 0
        for piece_name in list:
            if len(list[piece_name]) == 0:
                pass
            else:
                for piece_position in list[piece_name]:
                    if len(list[piece_name][piece_position]) == 0:
                        pass
                    else:
                        l+=1
                        break
                else:
                    continue
                break
        if l == 0:
            return {}
        return list

    def get_reverse_board(self):
        board_2 = []
        for i in range(8):
            temp = copy.deepcopy(self.board[8-i-1])
            temp.reverse()
            board_2.append(temp)
        return  board_2

    def get_position(self):
        l = {"R":"♖", "N":"♘", "B":"♗", "K":"♔", "Q":"♕", "P":"♙",
             "r":"♜", "n":"♞", "b":"♝", "k":"♚", "q":"♛", "p":"♟",
             "-":"-"}
        if self.colour == "black": # если ходят черные, переворачиваем доску
            board_ = self.get_reverse_board()
        else:
            board_ = self.board
        board_2 = [[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                if board_[i][j].colour == "black":
                    f = board_[i][j].name.lower()
                elif board_[i][j].colour == "white":
                    f = board_[i][j].name.upper()
                else:
                    f = "-"
                board_2[i].append(l[f])
        return board_2









if __name__ == "__main__":
    b = Board()
    b.make_a_starting_position()
    b.move(1, 0, 2, 0)
    b.cout(b.board)
    b.cout(b.get_reverse_board())
    print(b.get_position())
    print()
    print(b.all_possible_moves("white"))



class Data:
    """
    Класс отвечает за сохранение данных партий в файл
    и интерпретацию данных в файле
    """

    @staticmethod
    def save_data(file, board, game_data):
        """

        :param file: файл, в котором будет сохранена партия
        :param board: все фигуры на доске, у некоторых дополнительная информация
        (у короля и ладей - доступ к рокировке)
        :param game_data: Массив с информацией о важных
        аспектах игры (чей сейчас ход, доступно ли взятие на проходе,
        шах ли сейчас)
        :return:
        """
        with open(file, "w") as f:
            for argument in game_data:
                f.write(argument)

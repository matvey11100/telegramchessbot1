import json


class FieldNames:
    """
    Словарь для перевода из индексного обозначения
    полей в шахматную нотацию и наоборот
    """
    field_names = {}

    def create(self):
        for i in range(8):
            for j in range(8):
                self.field_names[str(i) + str(j)] = chr(j+ord('a')) + str(8-i)


if __name__ == "__main__":
    """
    Одноразово запускается, чтобы создать json файл
    с сопоставлением шахматной нотации и индексного
    обозначения полей
    """
    a = FieldNames()
    a.create()
    with open("FieldNames.json", "w") as f:
        json.dump(a.field_names, f)


class ConstantsReader:
    list_consts = []

    def __init__(self):
        try:
            with open('data\const.txt', "r") as file:
                for line in file:
                    self.list_consts.append(line)
        except FileNotFoundError:
            self.set_default_values()
            print('Файл const.txt не найден')

    def set_default_values(self):
        self.list_consts.append('1200')
        self.list_consts.append('800')

    def read_width(self) -> int:
        return int(self.list_consts[0])

    def read_height(self) -> int:
        return int(self.list_consts[1])

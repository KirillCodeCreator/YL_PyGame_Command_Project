class Scores:

    def __init__(self):
        pass

    def save_to_file(self, scores):
        try:
            with open('data/scores.txt', "w") as file:
                file.write(str(scores))
        except FileNotFoundError:
            print('Файл scores.txt не найден')

    def get_scores_from_file(self):
        try:
            with open('data/scores.txt', "r") as file:
                result = '0'
                for line in file:
                    result = line
                    break
                return result
        except FileNotFoundError:
            print('Файл scores.txt не найден')

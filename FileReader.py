import csv

class FileReader:

    words = []

    def read(self):
        with open('hangman_.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.words.append(row)
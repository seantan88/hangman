import csv

class FileReader:

    words = []

    def read(self):
        with open('hangman_wordbank.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for word in row:
                    self.words.append(word)

    def chooseWord(self):
    

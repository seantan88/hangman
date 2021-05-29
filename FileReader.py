import csv
import random

class FileReader:

    words = []

    def read(self):
        with open('hangman_wordbank.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for word in row:
                    self.words.append(word)


    def printWords(self):
        for word in self.words:
            print(word)

    def chooseWord(self):
        word = random.randrange(0,len(self.words))
        return self.words[word]
        


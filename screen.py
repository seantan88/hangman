from getpass import getpass
import os

class Screen:

    def clear(self):
        os.system('cls')

    phrase = str()
    blankPhrase = []

    def setPhrase(self):
        self.phrase = getpass("Please enter word\n\n")

    def getPhrase(self):
        return self.phrase

    def getBlanks(self):
        return self.blankPhrase

    def setBlanks(self, str):
        self.blankPhrase = str




    def createMan(self):
       head = ["  O"]
       neck = ["  |"]
       torsoArms = ["--|--"]
       legs = [" / /"]

       body = [head,neck,torsoArms,legs]
       return body
       
       
    def drawBody(self):
       body = self.createMan()
       for i in range(0, len(body)):
           print(", ".join(body[i]))
        
       print("\n\n")


    def getBlankLetters(self):
        blanks = []
        for i in range(0, len(self.phrase)):
            if (self.phrase[i] != ' '):
                blanks.append("_")
            else:
                blanks.append(" ")
        self.blankPhrase = blanks

    def drawBlanks(self):
        print(" ".join(self.blankPhrase))
        print("\n\n")



    def guessLetter(self):
        guess = str(input("Input a letter:\n\n"))
        indices = []
        if guess == "exit":
            exit()
        
        if len(guess) > 1:
            print("Please enter a character instead.")
            self.guessLetter

        for i in range(0, len(self.phrase)):
            if self.phrase[i] == guess:
                indices.append(i)
        
        if len(indices) > 0:
            for i in range(0, len(indices)):
                self.blankPhrase[indices[i]] = guess         
        else:
            print(guess + " does not occur")

    def guessSolve(self):
        indices = []
        solve = str(input("Input a word: \n\n"))
        if solve == "exit":
            exit()
        
        if len(solve) < 1: 
            print("Please enter a whole word instead.")
            self.guessSolve
        
        if self.phrase == solve:
            print("Congratulations you win!!! Poggers")
        
        if solve in self.phrase:
            index = self.phrase.index(solve)
        else:
            print("That word does not occur here!")
            return

        
        for i in range(index, index+len(solve)):
            self.blankPhrase[i] = self.phrase[i]


        







    def start(self):
        self.setPhrase()
        self.getBlankLetters()

    def run(self):
        self.drawBody()
        self.drawBlanks()
        self.guessSolve()
        self.run()



            


        
            
        
    
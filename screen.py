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



    def start(self):
        self.setPhrase()
        self.getBlankLetters()

    def run(self):
        self.drawBody()
        self.drawBlanks()
        self.guessLetter()
        self.run()



            


        
            
        
    
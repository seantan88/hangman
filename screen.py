from getpass import getpass

class Screen:

    phrase = str()
    blankPhrase = str()

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


    def getBlankLetters(self, phrase):
        phrase = str(phrase)
        blanks = []
        for i in range(0, len(phrase)):
            if (phrase[i] != ' '):
                blanks.append("_")
            else:
                blanks.append(" ")
        self.blankPhrase = blanks

    def drawBlanks(self):
        blanks = self.getBlankLetters(self.phrase)
        print(" ".join(self.blankPhrase))
        print("\n\n")



    def guessLetter(self):
        password = self.getPhrase()
        blanks = self.getBlanks()
        guess = str(input("Input a letter:\n\n"))
        if len(guess) > 1:
            print("Please enter a character instead.")
            self.guessLetter
        if guess in password:
            index = password.index(guess)
        tempStr = str()
        for i in range(0, len(guess)):
            if index == i:
                tempStr += guess
            else:
                tempStr += blanks[i]

        self.blankPhrase = tempStr

    def run(self):
        self.drawBody()
        self.setPhrase()
        self.drawBlanks()
        self.guessLetter()
        self.drawBlanks()



            


        
            
        
    
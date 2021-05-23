class Screen:

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
        return blanks

    def drawBlanks(self):
        phrase = str(input("Please enter word\n\n"))
        blanks = self.getBlankLetters(phrase)
        print(" ".join(blanks))
        print("\n\n")
            
        
    
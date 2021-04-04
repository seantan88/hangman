class Screen:

    def createMan(self):
       head = ["O"]
       neck = ["|"]
       torsoArms = ["--|--"]
       legs = ["/ /"]



       
       body = [head,neck,torsoArms,legs]
       for i in range(0, len(body)):
           print(", ".join(body[i]))

       
        
        
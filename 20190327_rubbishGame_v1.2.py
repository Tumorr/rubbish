from appJar import gui
import random

app=gui()
class Player:
    
    def __init__(self,name):
        self.name=name
        self.hp=10

    #5    
    def userChoiceConfirm(self):
        input_ = app.getEntry("input_")
        #move
        if input_ == "1":
            myMap.move()         
        #inspect
        elif input_ == "2":
            pass
        #heal up
        elif input_ == "3":
            pass
        else:
            pass
    #4
    def userChoice(self):
        app.clearEntry("input_")
        app.setLabel("text",'''What would you like to do?
        1. move
        2. inspect
        3. heal up''')
        app.showEntry("input_")       
        app.addButton("Confirm2",Player.userChoiceConfirm)      
        
    #3    
    def getNameCont(self):
        user = Player(app.getEntry("input_"))
        app.hideButton("Confirm")
        app.hideEntry("input_")
        Player.userChoice(self)        
    #2 
    def getName(self):
        app.hideButton("Continue")
        app.setLabel("text","Please, what is your name hero? ")
        app.addEntry("input_")
        app.addButton("Confirm",Player.getNameCont)
    #1    
    def start():
        app.addLabel("text","Hello there!\n\nI am Bolo, the leader of the lake dolphins that reside here in this Lake.\nThis lake has always been a safe haven for us lake dolphins.\nUntil recently that is, there have been rubbish monsters polluting our lake, taking their toll on our population.\nPlease help us, you must find and kill the rubbish king!")
        app.addButton("Continue",Player.getName)

class Map:
    def __init__(self):
        self.ROWS = 6
        self.COLUMNS = 6
        self.currentX = 0
        self.currentY = 0
        
    def direction(self):
        direction = app.getEntry("input_")
        if direction == "N":
            if self.currentY >= self.COLUMNS:
                #print("You are as far North as you can go")
                self.currentY = 6
            else:
                self.currentY += 1
        elif direction == "S":
            if self.currentY <= 0:
                print("You are as far South as you can go")
                self.currentY = 0
            else:
                self.currentY -= 1
        elif direction <= "E":
            if self.currentX == 0:
                print("You are as far East as you can go")
                self.currentX = 0
            else:
                self.currentX -= 1     
        elif direction == "W":
            if self.currentX >= self.ROWS:
                print("You are as far North as you can go")
                self.currentX = 6
                            
            else:
                self.currentY += 1
                            
        print("Your current location is:", self.getPosition())        
     
    def move(self):
        app.clearEntry("input_")
        app.hideButton("Confirm2")
        app.addButton("Confirm3",Map.direction)
        app.setLabel("text","Do you want to move N,S,E or W?")

                  
    def getPosition(self):
        currentPosition = "(" + str(self.currentX) + "," + str(self.currentY) + ")"
        return currentPosition
        

          
myMap = Map()
Player.start()
app.go()

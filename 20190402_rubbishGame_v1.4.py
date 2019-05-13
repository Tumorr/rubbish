from appJar import gui

app=gui()

class Player:
    
    def __init__(self,name):
        self.name=name
        self.hp=10

    #3    
    def userChoiceConfirm(self):
        userInput = app.getEntry("userInput")
        #move
        if userInput == "1":
            myMap.move()         
        #inspect
        elif userInput_ == "2":
            var=random.randint(1,3)
            if var == 1:
                meds=meds+1
            else:
                Player.userChoice(self)
        #heal up
        elif input_ == "3":
            pass
        else:
            pass
    #2
    def userChoice(self):
        app.showEntry("userInput")
        app.hideButton("btn2")
        myMap.getPosition()
        app.clearEntry("userInput")
        app.setLabel("label",'''What would you like to do?
        1. move
        2. inspect
        3. heal up''')
        try:
            app.addNamedButton("Confirm","btn3",Player.userChoiceConfirm)
            
        except ValueError:
            app.showButon("btn3")
     

    #1    
    def start():
        app.hideEntry("userInput")
        app.hideButton("btn1")
        app.clearEntry("userInput")
        app.setLabel("label","You there, traveller!\nIm so glad you stumbled upon our Village.\n\nI am Bolo, leader of the Dolphin clan that resides here in this village.\nWe have recently been under siege by an army of rubbish.\nPlease help us, you must find and kill the rubbish king!\n\nDo you accept this mission hero?")
        app.addNamedButton("Accept","btn2",Player.userChoice)
        
class Map:
    def __init__(self):
        self.ROWS = 6
        self.COLUMNS = 6
        self.currentX = 0
        self.currentY = 0
        
    def direction(self):
        direction = app.getEntry("userInput")
        if direction == "N":
            if self.currentY >= self.COLUMNS:
                #print("You are as far North as you can go")
                self.currentY = 6
            else:
                self.currentY += 1
        elif direction == "S":
            if self.currentY <= 0:
                #print("You are as far South as you can go")
                self.currentY = 0
            else:
                self.currentY -= 1
        elif direction <= "E":
            if self.currentX == 0:
                #print("You are as far East as you can go")
                self.currentX = 0
            else:
                self.currentX -= 1     
        elif direction == "W":
            if self.currentX >= self.ROWS:
                #print("You are as far North as you can go")
                self.currentX = 6
                            
            else:
                self.currentY += 1
                            
        print("Your current location is:", self.getPosition())        
     
    def move(self):
        app.clearEntry("userInput")
        app.hideButton("btn3")
        app.addNamedButton("Confirm","btn4",myMap.direction)
        app.setLabel("label","Do you want to move N,S,E or W?")

                  
    def getPosition(self):
        currentPosition = "(" + str(self.currentX) + "," + str(self.currentY) + ")"
        return currentPosition

def setUser(user):    
    user = app.getEntry("userInput")
    Player.start()

myMap=Map()
app.addLabel("label","Enter your name: ")
app.addEntry("userInput")
app.addNamedButton("Continue","btn1",setUser)


app.go()
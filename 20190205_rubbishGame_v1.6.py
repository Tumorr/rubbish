#import libraries 
from appJar import gui
import random
import time
#creates gui
app=gui("rubbishGame")
app.setSize(600,200)
app.setFont(12)
app.setLabelFont(14)
app.setImageLocation(r"C:\Users\15358\map")

class Player:
      
    def __init__(self):
        self.hp=10
        self.meds=0
        self.weapon=0
    #5
    def userChoiceConfirm(self):
        Player.playerButtons()
        userInput = app.getEntry("userInput")
        #move
        if userInput == "1":
            myMap.move()         
        #inspect
        elif userInput == "2":
            app.hideEntry("userInput")            
            var=random.randint(1,4)
            if var == 1:
                app.setLabel("label","You look around,\nfinding a bandage on the floor.")
                Player.playerButtons()
                app.showButton("btn5")
                Player.meds += 1
            
            else:
                var=random.randint(1,3)
                if var==1:
                    app.setLabel("label","You look around,\npuddles and waste,\nnothing else.")
                else:
                    app.setLabel("label","You look around,\nsmelling rotten flesh you recoil,\nyou move on, finding nothing.")                    
                Player.playerButtons()
                app.showButton("btn5")                
        #heal up
        elif userInput == "3":
            pass
        else:
            app.errorBox("error","Invalid Input")
            Player.userChoice(self)
        app.showEntry("userInput")
    #4
    def userChoice(self):
        app.showEntry("userInput")
        myMap.getPosition()
        app.clearEntry("userInput")
        app.setLabel("label",'''What would you like to do?
        1) Move
        2) Inspect
        3) Heal up''')
        Player.playerButtons()
        app.showButton("btn3")  
        app.showSubWindow("map")
     

    #3 - Introductory diaglogue	   
    def start():
        app.hideEntry("userInput")
        app.hideButton("btn1")
        app.clearEntry("userInput")
        app.setLabel("label","Help, \nyou must, please\n\nThe rubbish, its everywhere\nhalf of my village has fallen, they're taking over\nif this doesnt stop, us dolphins will fall extinct\n\nWe know of four camps, each located in different corners of our island.\nPlease hero, do you accept this task?")
        Player.playerButtons()
        app.showButton("btn2")
        
        
    def playerButtons():
        Player.removePlayerButtons()
        #located in start(defined in Player), leads to user choice
        app.addNamedButton("Accept","btn2",Player.userChoice)
        app.hideButton("btn2")
        #located in userChoice(Player), leads to userChoiceConfirm / depends on input
        app.addNamedButton("Confirm","btn3",Player.userChoiceConfirm)
        app.hideButton("btn3")        
        #located in userChoiceConfirm
        app.addNamedButton("Continue","btn5",Player.userChoice)
        app.hideButton("btn5")
    
    def removePlayerButtons():
        try:
            app.removeButton("btn2")
        except:
            pass
        try:
            app.removeButton("btn3")
        except:
            pass
        try:
            app.removeButton("btn5")
        except:
            pass
class Map:
    def __init__(self):
        self.currentX = 0
        self.currentY = 0
        
    def direction(self):
        direction = app.getEntry("userInput")
        if direction == "N":
            if self.currentY >= 3:
                app.setLabel("label","You are as far North as you can go.")
                self.currentY = 3
                app.showButton("btn5")                
            else:
                self.currentY += 1
                Player.userChoice(self)                
        elif direction == "S":
            if self.currentY <= -3:
                app.setLabel("label","You are as far South as you can go.")
                self.currentY = -3
            else:
                self.currentY -= 1
                Player.userChoice(self)                
        elif direction == "E":
            if self.currentX >= 3:
                app.setLabel("label","You are as far East as you can go.")
                self.currentX = 3
                app.showButton("btn5")
                
            else:
                self.currentX += 1
                Player.userChoice(self)                
        elif direction == "W":
            if self.currentX <= -3:
                app.setLabel("label","You are as far West as you can go.")
                self.currentX = -3
                app.showButton("btn5")                
            else:
                self.currentX -= 1
                Player.userChoice(self)                
        app.hideButton("btn4")
        #updates coords on the map
        app.setLabel("x,y", myMap.getPosition())
        
        def mapImageRefresh(self):
            if self.currentX== -3:
                if self.currentY== -3:
                    pass
                if self.currentY== -2:
                    pass
                if self.currentY == -1:
                    pass
                if self.currentY== 0:
                    pass
                if self.currentY== 1:
                    pass
                if self.currentY== 2:
                    pass
                if self.currentY== 3:
                    pass
                
            if self.currentX== -2:
                pass
            
            if self.currentX== -1:
                pass
            
            if self.currentX== 0:
                pass
            
            if self.currentX== 1:
                pass
            
            if self.currentX== 2:
                pass
            
            if self.currentX == 3:
                pass
        

    def move(self):
        app.clearEntry("userInput")
        app.setLabel("label","Do you want to move N,E,S or W?")
        Map.mapButtons()
        app.showButton("btn4")
        
        
                  
    def getPosition(self):
        currentPosition = "(" + str(self.currentX) + "," + str(self.currentY) + ")"
        return currentPosition
    
    def mapButtons():
        Map.removeMapButtons()
        #located in move(Map), leads to direction
        app.addNamedButton("Confirm","btn4",myMap.direction)
        app.hideButton("btn4")
    
    def removeMapButtons():
        try:
            app.removeButton("btn4")
        except:
            pass
   
        
#2 - Sets user, starts game
def setUser(user):    
    user = app.getEntry("userInput")
    Player.start()
    
            
#1
myMap=Map()
#First label seen
app.addLabel("label","Name: ")
#Takes user input, used throughout the code
app.addEntry("userInput")
app.addNamedButton("Continue","btn1",setUser)
app.setBg("Light Blue")
#Label later used to display x and y values


app.startSubWindow("map",modal=False)
app.setBgImage("00.png")
app.setSize(400,400)
app.addLabel("coordinates","Coordinates: ") 
app.addLabel("x,y", myMap.getPosition())
app.stopSubWindow()

#starts the gui
app.go()
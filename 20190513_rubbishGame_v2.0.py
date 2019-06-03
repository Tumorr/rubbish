#import libraries 
from appJar import gui
#random used for luck based loot
import random

#create gui
app=gui("rubbishGame")
app.setSize(300,300)
app.setFont(12)
app.setLabelFont(10)

#formatting
app.setSticky("news")
app.setExpand("both")


class Player:
       def  __init__(self):
              healthPoints=0
              meds=0
       
       def updateMeds(self):
              meds+=1
              app.setLabel("medsValue",meds)
              

def displayMeds():
        try:
                app.addLabel("meds","Bandages :")
                app.addLabel("medsValue",0)
                
        except:
                pass        
        
        
#called after user enters and confirms move,inspect,healup
def userChoiceConfirm():
        #adds and updates meds value
        displayMeds()
        #updates xy values on screen
        Map.xy()       
        #deletes and recreates all buttons outside of a class - Ensures buttons are not created twice
        buttons()
        
        #gets user input, sets it to a variable
        userInput = app.getEntry("userInput")
        
        #move
        if userInput == "1":  
                #here they enter NESW
                myMap.move()
            
        #inspect
        elif userInput == "2":
                app.clearEntry("userInput")
                app.hideEntry("userInput")
                #66% chance to find loot
                rng=random.randint(1,4)
                rngList1=[1,2]
                if rng in rngList1:
                       app.setLabel("label","You look around,\nfinding a bandage on the floor.")
                       buttons()
                       app.showButton("btn5")
                       Player.updateMeds(self)

                else:                                                           
                       #two different outputs when user doesnt find loot
                       rng=random.randint(1,2)
                       if rng==1:
                              app.setLabel("label","You look around,\npiles of waste,\ntheres nothing useful.")
                              buttons()
                              app.showButton("btn5")
                       else:
                              app.setLabel("label","You inspect the area,\nfinding nothing.")                    
                              buttons()
                              app.showButton("btn5")                
        #when user enters invalid input        
        else:   
                app.errorBox("error#2","Invalid Input")
                userChoice(self)                
    
    #Called after introductory dialogue and after user moves
def userChoice(self):
        #Updates xy
        try:
                app.setLabel("xy", myMap.getPosition()) 
        except:
                pass
        
        app.showEntry("userInput")
        myMap.getPosition()
        app.clearEntry("userInput")
        app.setLabel("label",'''What would you like to do?
        1) Move
        2) Inspect
        3) Heal''')
        buttons()
        app.showButton("btn3")

     

    #3 - Introductory diaglogue	   
def start():
        app.hideEntry("userInput")
        app.hideButton("btn1")
        app.clearEntry("userInput")
        app.setLabel("label","Help us please,\n\nThe rubbish, its everywhere\nhalf of my village has fallen, they're taking over\nif this doesnt stop, us dolphins will fall extinct\n\n'something about your objective'")
        buttons()
        app.showButton("btn2")

        
    #deletes and recreates buttons  
def buttons():
        removeButtons()
        #located in start, leads to user choice
        app.addNamedButton("Accept Mission","btn2",userChoice)
        app.hideButton("btn2")
        #located in userChoice, leads to userChoiceConfirm / depends on input
        app.addNamedButton("Confirm","btn3",userChoiceConfirm)
        app.hideButton("btn3")        
        #located in userChoiceConfirm
        app.addNamedButton("Continue","btn5",userChoice)
        app.hideButton("btn5")
    
    #tries deleting buttons, found in buttons()
def removeButtons():
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
        
    #coordinates
        def __init__(self):
                self.currentX = 0
                self.currentY = 0
                self.hp1 = 5
                self.hp2 = 5
                self.hp3 = 10
                self.hp4 = 10
        def xy():
                try:
                        app.addLabel("coords","Coordinates: ")
                        app.addLabel("xy",myMap.getPosition())
                        
                except:
                        app.setLabel("xy", myMap.getPosition())                        
                        
                
    
    #called from move, changes xy values based on input, prevents user from exceeding max xy values
    #else = if value doesnt exceed barrier user can move
        def direction(self):
                direction = app.getEntry("userInput")
                if direction == "N":
                        if self.currentY >= 2:
                                app.hideEntry("userInput")                                
                                app.setLabel("label","You are as far North as you can go.")
                                self.currentY = 2
                                app.showButton("btn5")                
                        else:
                                self.currentY += 1
                                userChoice(self)                
                elif direction == "S":
                        if self.currentY <= -2:
                                app.hideEntry("userInput")                                
                                app.setLabel("label","You are as far South as you can go.")
                                self.currentY = -2
                        else:
                                self.currentY -= 1
                                userChoice(self)                
                elif direction == "E":
                        if self.currentX >= 2:
                                app.hideEntry("userInput")                                
                                app.setLabel("label","You are as far East as you can go.")
                                self.currentX = 2
                                app.showButton("btn5")
                
                        else:
                                self.currentX += 1
                                userChoice(self)                
                elif direction == "W":
                        if self.currentX <= -2:
                                app.hideEntry("userInput")                                
                                app.setLabel("label","You are as far West as you can go.")
                                self.currentX = -2
                                app.showButton("btn5")                
                        else:
                                self.currentX -= 1
                                userChoice(self)                
        #deals with invalid input
                else:
                        app.errorBox("error","Invalid Input")
                        move(self)
            
                app.hideButton("btn4")
                #updates coords on the map
        
        def enemy(self,healthPoints):
                
                #MAP IS 5x5, THESE ARE CORNERS
                if self.currentX== -2:
                        if self.currentY== -2:
                                #try:
                                app.addLabel("boss#1","Boss #1 Health: ")
                                app.addLabel("hp#1",self.hp1)
                                #except:
                                 #       app.showLabel("boss#1")
                                  #      app.showLabel("hp#1")
                                   #     app.setLabel("hp#1",self.hp1)
                        else:
                                app.hideLabel("hp#1")                                
                                        
                                                                
                        if self.currentY== 2:
                                try:
                                        app.addLabel("boss#2","Boss #2 Health: ")
                                        app.addLabel("hp#2",self.hp2)
                                except:
                                        app.showLabel("boss#2")
                                        app.showLabel("hp#2")
                                        app.setLabel("hp#2",self.hp2)
                        else:
                                app.hideLabel("hp#2")
                                        
                        
                        healthPoints-=1
                        
                        app.setLabel("label",'''What would you like to do?
                               1) Run
                               2) Attack
                               3) Heal''')                        

                if self.currentX== 2:
                        if self.currentY== -2:
                                try:
                                        app.addLabel("boss#3","Boss #3 Health: ")
                                        app.addLabel("hp#3",self.hp3)
                                except:
                                        app.showLabel("boss#3")
                                        app.showLabel("hp#3")
                                        app.setLabel("hp#3",self.hp3)
                        else:
                                app.hideLabel("hp#3")
                        
                                                                
                        if self.currentY== 2:
                                try:
                                        app.addLabel("boss#4","Boss #4 Health: ")
                                        app.addLabel("hp#4",self.hp4)
                                except:
                                        app.showLabel("boss#4")
                                        app.showLabel("hp#4")
                                        app.setLabel("hp#4",self.hp4)
                        else:
                                app.hideLabel("hp#3")
                                
                                        
                        
                        healthPoints-=1
                        
                        app.setLabel("label",'''What would you like to do?
                               1) Run
                               2) Attack
                               3) Heal''') 
        

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

def setUser(user):
        user = app.getEntry("userInput")
        if user=="":
                try:
                        app.addLabel("nameerror","Please enter a Username")
                except:
                        pass
        else:
                start()
                try:
                        app.hideLabel("nameerror")
                except:
                        pass

#1
myMap=Map()
#First label seen
app.addLabel("label","Username: ")
#Takes user input, used throughout the code
app.addEntry("userInput")
app.addNamedButton("Continue","btn1",setUser)
app.setBg("Light Blue")

#starts the gui
app.go()

#enemy in each corner, while xy values are equal to the corners, a label appears displaying a health bar, your options change into 1) Run 2) Attack
#3(heal) doesnt need to change
#when xy @desired values 2 will lower the health points of whatever boss you're attacking
#when you move onto these coordinates you lose 1 health, you also lose 1 hp after attacking 
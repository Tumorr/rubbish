#import needed libraries
from appJar import gui
import random

app = gui()


class Player:
          def __init__(self, name):
                    self.name = name
                    self.hp = 10
                    self.meds = 5          
          
          def confirmName(self):
                    user = Player(app.getEntry("input_"))
                    app.hideButton("Confirm")
                    app.hideEntry("input_")
                    Player.userChoice(self)
         
          def next_():
                    
                    app.hideButton("Continue")
                    app.setLabel("text","What is your name Traveller? ")
                    app.addEntry("input_")
                    app.addButton("Confirm", Player.confirmName)  
                    
          def start():
                    app.addLabel("text","Hello there!\n\nI am Bolo, leader of the dolphins that reside here in Lake Snihplod.\nLake Snihplod has always been a safe haven for dolphins from all over.\nThis was until recently when rubbish monsters started making their way into the lake and reeking havoc on our underwater village.\nThere have been many fatalities, you must find and kill their leader,  P. Murt!")
                    app.addButton("Continue",Player.next_)                    
     
     
          def showStats(self):
                    app.addlabel("name",self.name)
                    app.addLabel("hp",self.hp)

     
          def userChoice(self):
                    app.setLabel("text",'''What would you like to do?
                    1. move
                    2. inspect
                    3. heal up''')
                    app.clearEntry("input_")
                    app.showEntry("input_")
                    app.addButton("Confirm2",Player.userChoiceConfirm)
                    input_ = app.getEntry("input_")
                    global input_
          
          def userChoiceConfirm(self):
                    if input_ == "1":
                              myMap.move()
                    elif input_ == "2":
                              app.addLabel("inspectChoice","You inspected the area")
                    elif input_ == "3":
                              app.addLabel("healChoice","You took time to heal up")
                    elif input_ != ("1","2","3"):
                              app.addLabel("notOption","That was not an option.")
                              #self.userChoice(self)
                              
          def attack(self):
                    app.addLabel("attack","You attacked the zombie!")
     
          def defend(self):
                    app.addLabel("defend","You protected yourself against the zombie")
     
          def heal(self):          
                    app.addLabel("heal","You healed yourself")
     
          def takeAttack(self):
                    app.addLabel("You lost some health")
                    self.hp -= 2

class Map:
          def __init__(self):
                    self.ROWS = 6
                    self.COLUMNS = 6
                    self.currentX = 0
                    self.currentY = 0
     
          def move(self):
                    app.addLabel("nsew","Do you want to move N,S,E or W?")
                    app.addEntry("direction")
                    direction = app.getEntry("direction")
                    if direction == "N":
                              if self.currentY >= self.COLUMNS:
                                        app.addLabel("farNorth","You are as far North as you can go")
                                        self.currentY = 6
                              else:
                                        self.currentY += 1
                    elif direction == "S":
                              if self.currentY <= 0:
                                        app.addLabel("farSouth","You are as far South as you can go")
                                        self.currentY = 0
                              else:
                                        self.currentY -= 1
                    elif direction <= "E":
                              if self.currentX == 0:
                                        app.addLabel("farEast","You are as far East as you can go")
                                        self.currentX = 0
                              else:
                                        self.currentX -= 1     
                    elif direction == "W":
                              if self.currentX >= self.ROWS:
                                        app.addLabel("farNorth","You are as far North as you can go")
                                        self.currentX = 6
                    
                              else:
                                        self.currentY += 1
                    
                              app.addLabel("yourLocation","Your current location is:", self.getPosition())
          
          def getPosition(self):
                    currentPosition = "(" + str(self.currentX) + "," + str(self.currentY) + ")"
                    return currentPosition



myMap = Map()
Player.start()
#must be at the bottom
app.go()

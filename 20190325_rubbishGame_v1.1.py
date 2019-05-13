from appJar import gui
import random

app=gui()
class Player:
    def __init__(self,name):
        self.name=name
        self.hp=10
        self.meds=0
        
        #4
        def userChoice():
            app.clearEntry("input_")
            app.setLabel("text",'''What would you like to do?
            1. move
            2. inspect
            3. heal up''')
            app.showEntry("input_")
            app.addButton("Confirm2",Player.userChoiceConfirm)
            input_ = app.getEntry("input_")
            #global input_        
        
    #3    
    def getNameCont():
        user = Player(app.getEntry("input_"))
        app.hideButton("Confirm")
        app.hideEntry("input_")
        Player.userChoice(self)        
    #2 
    def getName():
        app.hideButton("Continue")
        app.setLabel("text","What is your name Traveller? ")
        app.addEntry("input_")
        app.addButton("Confirm",Player.getNameCont)
    #1    
    def start():
        app.addLabel("text","Hello there!\n\nI am Bolo, leader of the dolphins that reside here in Lake Snihplod.\nLake Snihplod has always been a safe haven for dolphins from all over.\nThis was until recently when rubbish monsters started making their way into the lake and reeking havoc on our underwater village.\nThere have been many fatalities, you must find and kill their leader,  P. Murt!")
        app.addButton("Continue",Player.getName) 

Player.start()
app.go()

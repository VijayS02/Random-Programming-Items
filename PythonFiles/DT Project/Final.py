#Anything starting with "#" is a comment, python does not execute comments
import RPi.GPIO as GPIO #Raspberry pi GPIO api import
import time #Python time module for delays
from skpy import Skype #Skype API
from skpy import SkypeEventLoop #Skype event handler api
from datetime import datetime, time #DateTime Api
GPIO.setmode(GPIO.BCM) #Set the board pin type
solenoid = 21 #Solenoid + volts pin
contact = 26 #Contact pad input PIN
GPIO.setup(solenoid,GPIO.OUT) #Set solenoid (21) as output pin
GPIO.setup(contact,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Set contact (26) as input pin
User = "<INSERT USER ID HERE>" #The User's Skype ID

now = datetime.now() #Get the current line
me = Skype("<USERNAME>","<PASSWORD>") #Login to skype on bot

def checkClosed(): #Subprogram to check if door is closed.
    doorVal = GPIO.input(contact) #Is there current flowing through the contact pads?
    if(doorVal == True):
        return True#If there is then return true
    return False #Otherwise return false


def lock(): #Lock the door
    for i in range(0,5): #Loop 5 times
        if(checkClosed() == True): #Is the door closed
            GPIO.output(solenoid,0) #IF so then release solenoid
            return 0 #End subprogram
        time.sleep(10) #Wait 10 seconds
    msg(User,me,"Unable to close door, please check if it is closed.") #If loop ends after 5 tries then send warning to user.


def unlock(): #Unlock door
        GPIO.output(solenoid,1) #Retract Solenoid
        msg(User,me,"Unlocked.") #Tell the user it has been unlocked
        time.sleep(10) #Wait 10 seconds
        lock()

def status():
        PCB = GPIO.input(solenoid)
        if(PCB == 1):
            PCB = True
        else:
            PCB = False
        door = checkClosed()
        msg(User,me,str("Lock on: " + str(PCB) + " & Door closed: " + str(door)))

        
def msg(usr,skyp,message):
     try:
          if(usr == False):
               print("No user declared yet.")
          tmpid = str("8:"+usr)
          skyp.chats[tmpid].sendMsg(message)
     except:   
          print("Unable to get user.")
     

def refresh():
        doorVal = checkClosed()
        if(doorVal == True):
            if(GPIO.input(solenoid) == 1):
                GPIO.output(solenoid,0)
            else:
                msg(User,me,"Door is closed.")
        else:
            msg(User,me,"Door is currently open.")

class MySkype(SkypeEventLoop):
     def onEvent(self, event):
       (repr(event))
       current = datetime.now()
       if((current - now).seconds> 20 and event.type == "NewMessage" and event.msg.user.id == "<Insert User ID here>" ):
          try:
                 user = event.msg.user.id
                 if(event.msg.content.replace(" ","").lower() == "lock"):
                      print("Locking")
                      lock()
                      print("Locked!")
                      msg(user,me,"Locked.")
                 elif(event.msg.content.replace(" ","").lower() == "unlock"):
                      print("Unlocking")
                      unlock()
                      msg(user,me,"Locked.")
                      print("Locked!")
                 elif(event.msg.content.replace(" ","").lower() == "status"):
                      status()
                 elif(event.msg.content.replace(" ","").lower() == "refresh"):
                      refresh()
                      

          except Exception as e:
                  pass


test =MySkype("vijaythepro","born0609", autoAck=True)
test.loop()
#lock()
#GPIO.cleanup()
#msg("live:75b61edbb44e4d3",me,"locked.")



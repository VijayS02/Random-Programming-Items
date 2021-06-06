# Anything starting with "#" is a comment, python does not execute comments
import RPi.GPIO as GPIO  # Raspberry pi GPIO api import
import time  # Python time module for delays
from skpy import Skype  # Skype API
from skpy import SkypeEventLoop  # Skype event handler api
from datetime import datetime, time  # DateTime Api

GPIO.setmode(GPIO.BCM)  # Set the board pin type
solenoid = 21  # Solenoid + volts pin
contact = 26  # Contact pad input PIN
GPIO.setup(solenoid, GPIO.OUT)  # Set solenoid (21) as output pin
GPIO.setup(contact, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set contact (26) as input pin
User = "<INSERT USER ID HERE>"  # The User's Skype ID

now = datetime.now()  # Get the current line
me = Skype("<USERNAME>", "<PASSWORD>")  # Login to skype on bot


def checkClosed():  # Subprogram to check if door is closed.
    doorVal = GPIO.input(contact)  # Is there current flowing through the contact pads?
    if (doorVal == True):
        return True  # If there is then return true
    return False  # Otherwise return false


def lock():  # Lock the door
    for i in range(0, 5):  # Loop 5 times
        if (checkClosed() == True):  # Is the door closed
            GPIO.output(solenoid, 0)  # IF so then release solenoid
            return 0  # End subprogram
        time.sleep(10)  # Wait 10 seconds
    msg(User, me,
        "Unable to close door, please check if it is closed.")  # If loop ends after 5 tries then send warning to user.


def unlock():  # Unlock door
    GPIO.output(solenoid, 1)  # Retract Solenoid
    msg(User, me, "Unlocked.")  # Tell the user it has been unlocked
    time.sleep(10)  # Wait 10 seconds
    lock()  # Lock the solenoid (Subprogram)


def status():  # Check the status
    PCB = GPIO.input(solenoid)  # Is the solenoid output on?
    if (PCB == 1):  # If so then
        PCB = True  # Set variable PCB to true
    else:  # Otherwise
        PCB = False  # Set variable PCB to False
    door = checkClosed()  # Store the door closed value into a variable (subprogram)
    msg(User, me, str("Lock on: " + str(PCB) + " & Door closed: " + str(door)))  # Send message to user about info.


def msg(usr, skyp, message):  # Send a message to user via skype
    try:
        tmpid = str("8:" + usr)  # Get the user's chat id
        skyp.chats[tmpid].sendMsg(message)  # Send the message
    except:
        print("Unable to connect.")  # If error is thrown. Send warning to console.


def refresh():  # Refresh the current status
    doorVal = checkClosed()  # Check the door status
    if (doorVal == True):  # if door is closed
        if (GPIO.input(solenoid) == 1):  # Is solenoid on?
            GPIO.output(solenoid, 0)  # Turn it off
        else:
            msg(User, me, "Door is closed.")  # otherwise send message to user
    else:
        msg(User, me, "Door is currently open.")  # If door is open send message to user.


class MySkype(SkypeEventLoop):  # Skype event handler loop
    def onEvent(self, event):
        (repr(event))
        current = datetime.now()
        if ((
                current - now).seconds > 20 and event.type == "NewMessage" and event.msg.user.id == User):  # If 20 seconds has passed since program started and the type of event is a new message and the message is from user
            try:
                if (event.msg.content.replace(" ", "").lower() == "lock"):# If message is lock
                    print("Locking") #Send lock to console
                    lock() #Call lock subprogram
                    print("Locked!")#Send locked to console
                    msg(User, me, "Locked.") #Send locked to user.
                elif (event.msg.content.replace(" ", "").lower() == "unlock"): #If message is unlock
                    print("Unlocking") #Send unlocking to console
                    unlock() #Call unlock subprogram
                    msg(User, me, "Locked.") #Send locked to user. (The unlock subprogram auto locks after 10 seconds if possible)
                    print("Locked!") #Send Locked to console
                elif (event.msg.content.replace(" ", "").lower() == "status"): #If message is status
                    status() #Call status subprogram
                elif (event.msg.content.replace(" ", "").lower() == "refresh"):#If message is refresh
                    refresh()#Call refresh subprogram


            except Exception as e:
                print(e) #Print any errors to console but dont stop program if error occurs.


test = MySkype("<USERNAME>", "<PASSWORD>", autoAck=True) #Login to skype (Bot side) This time for event loop
test.loop() #Call loop ( Main program)



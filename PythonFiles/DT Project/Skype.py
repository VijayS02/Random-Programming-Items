from skpy import Skype
from skpy import SkypeEventLoop
from datetime import datetime, time

now = datetime.now()
me = Skype("vijaythepro","born0609")
user = False


def msg(usr,skyp,message):
     try:
          if(usr == False):
               print("No user declared yet.")  
          tmpid = str("8:"+usr)
          skyp.chats[tmpid].sendMsg(message)
     except:   
          print("Unable to get user.")
     


class MySkype(SkypeEventLoop):
     def onEvent(self, event):
       (repr(event))
       current = datetime.now()
       if((current - now).seconds> 20 and event.type == "NewMessage"):
          try:
                 user = event.msg.user.id
                 if(event.msg.content == "lock"):
                      print("LOCKING!")
                      msg(user,me,"Locked.")

          except Exception as e:
                  #print(e)
               pass


test =MySkype("vijaythepro","born0609", autoAck=True)
test.loop()
#msg("live:75b61edbb44e4d3",me,"locked.")


import os
import re
import datetime as da
if((int(da.datetime.now().strftime("%H"))>7 and int(da.datetime.now().strftime("%H"))<18) or int(da.datetime.now().strftime("%H"))>20):
     directory = 'D:\Program Files\SteamLibrary\steamapps\common\\'
     file = open('testfile.txt','r')

     info = file.read()
     info = info.split('\n')
     info.pop()
     file.close()
     print(info)
     for i in info:
          info[info.index(i)] = i.split('|')
     for i in info:
          for x in i:
               info[info.index(i)][info[info.index(i)].index(x)] = x.split(',')
     
     for i in info:
          for x in i[1]:
               os.rename((directory+i[0][0]+'\\'+i[2][i[1].index(x)]),(directory+i[0][0]+'\\'+x))
     print(info)

          
     file = open('testfile.txt','w')
     file.write('')
     file.close()
else:
     print("Not now Vijay.")
     input(" :) " )

import string
import random
import os

def randomNameGen(origName):
    ext = ''
    try:
        ext = origName[origName.index('.'):len(origName)]
    except ValueError:
        print('')
    renameStr = ''
    for i in range(0,20):
        renameStr = renameStr+ random.choice(string.ascii_letters)
    return renameStr+ext

def appendinfoToFile(folderName,infLst):
    origNames = '|'
    renames = '|'
    for i in infLst[0]:
        origNames = origNames +','+ str(i)
    for i in infLst[1]:
        renames = renames +','+ str(i)
    actual = folderName+origNames+renames
    readF = open('testfile.txt','r')
    temp1 = readF.read()
    readF.close()
    file = open('testfile.txt','w')
    tempWrite = str(actual +'\n'+temp1)
    file.write(tempWrite)
    file.close()
    
def listRnamer(directory):
    files = os.listdir(directory)
    names = [files,[]]
    for i in files:
        names[1].append(randomNameGen(i))
    return names

def Renamer(folderN,directory):
    temp = directory+folderN
    print("Storing info...")
    tempVals= listRnamer(temp)
    appendinfoToFile(folderN,tempVals)
    print("Renaming...")
    for i in tempVals[0]:
        curFile = temp+'\\'+str(i)
        os.rename(curFile,temp+'\\'+tempVals[1][tempVals[0].index(i)])
    print("Complete.")

for i in os.listdir('D:\Program Files\SteamLibrary\steamapps\common\\'):
    Renamer(i,'D:\Program Files\SteamLibrary\steamapps\common\\')

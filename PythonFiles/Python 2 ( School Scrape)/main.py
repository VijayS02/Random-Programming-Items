import sys
import arrow
from datetime import datetime
from pytz import UTC # timezone
from ics import Calendar,Event
from urllib.request import urlopen
file = open("data2BAK.txt")
data = file.read()
file.close()
data = data.split("\n")
for i in range(0,len(data)):
    temp = data[i].split(",")
    lessons = []
    if("[" in temp[1]):
        brak = temp[1][temp[1].index("["):len(temp[1])-1]
        udat = []
        if( "R" in brak or "N" in brak or "C" in brak or "U" in brak):
            
            brak = brak.replace("]","")
            udat.append(brak[1:3])
            udat.append(brak[3:len(brak)])
            udat.append(temp[1][0:temp[1].index("[")])
            temp[1] = udat
    try:
        temp[len(temp)-1] = temp[len(temp)-1].split("|")
        count = 0
        for z in temp[len(temp)-1]:
            z = z.split("-")
            count2 = 0
            for x in z:
                if(len(x)>8):
                    
                    x = x.split(" ")
                    if((x[0] in lessons) == False):
                        lessons.append(x[0])
                elif((x in lessons) == False and ("STUDYP" in x)==False):
                        lessons.append(x)
                z[count2] = x    
                count2 +=1
            temp[len(temp)-1][count] = z
            count+=1
    except:
        print("fail")
    temp.append(lessons)
    data[i] = temp

def binSearch(dat,src,start,stop):
    mid = int((stop-start)/2) + start
    if(int(dat[mid][0]) == src):
        return dat[mid]
    elif(int((stop-start)/2) <=1):
        return -1
    elif(int(dat[mid][0])>src):
        return binSearch(dat,src,start,mid)
    elif(int(dat[mid][0])<src):
        return binSearch(dat,src,mid,stop)
        

#sys.setrecursionlimit(1500)
#print(binSearch(data,8034,0,len(data)-1))   
def getData(name,sid):
    psLst = []
    if(name == None):
        t = binSearch(data,8034,0,len(data)-1)
        if(t ==-1):
            print("No matches")
        else:
            return t
    else:
        for i in data:
            if(len(i[1]) == 3 and name.lower().replace(" ","") in i[1][2].lower().replace(" ","")):
                psLst.append(i)
                print(str(psLst.index(i) +1) +") "+' '.join(i[1]))
            elif(name in i[1]):
                
                psLst.append(i)
                print(str(psLst.index(i) +1) +") "+i[1])
    if(len(psLst)>1):
        return psLst[int(input("Which one?Number\n"))-1]
    elif(len(psLst)==0):
        return None
    elif(len(psLst)==1):
        return psLst[0]
    else:
        print("No values to match: ",name)
        return psLst[0]

def wkNumToEng(num):
    if(num == 0):
        return "Monday"
    elif(num == 1):
        return "Tuesday"
    elif(num == 2):
        return "Wednesday"
    elif(num==3):
        return "Thursday"
    elif(num==4):
        return "Friday"
def matchPeriodsNoPrint(per1,per2):
    if(len(per1[len(per1)-2]) == 10 and len(per2[len(per2)-2]) == 10):
        matches = []
        for x in range(0,10):
            for z in range(0,5):
                if(per1[len(per1)-2][x][z] == per2[len(per2)-2][x][z]):
                    matches.append([x,z,per2[len(per2)-2][x][z]])
                    #print("Week " + str((x//5)+1) + "| "+wkNumToEng(x-((x//5)*5)) + "  | Period " + str(z+1),per2[len(per2)-2][x][z])
        return matches
    else:
        print("One or more data is incorrect")
        return None

def matchPeriods(per1,per2):
    if(len(per1[len(per1)-2]) == 10 and len(per2[len(per2)-2]) == 10):
        matches = []
        for x in range(0,10):
            for z in range(0,5):
                if(per1[len(per1)-2][x][z] == per2[len(per2)-2][x][z]):
                    matches.append([x,z,per2[len(per2)-2][x][z]])
                    print("Week " + str((x//5)+1) + "| "+wkNumToEng(x-((x//5)*5)) + "  | Period " + str(z+1),per2[len(per2)-2][x][z])
        if(len(matches)==0):
            print("No similar lessons.")
        else:
            print(str(len(matches)) + " lessons at the same time")
        return matches
    else:
        print("One or more data is incorrect")
        return None
    
def classListNoPrint(clCode):
    ret = []
    for i in data:
     if(len(i[len(i)-1])!=0):
         if(clCode in i[len(i)-1]):
                if(len(i[1])==3 and i[1][0] == clCode[0:2]):
                    ret.append(i)
                    #print(i)
                elif(len(i[1])!=3):
                    #print(i)
                    ret.append(i)
    return ret

def classList(clCode):
    #ret = []
    for i in data:
     if(len(i[len(i)-1])!=0):
         if(clCode in i[len(i)-1]):
                if(len(i[1])==3 and i[1][0] == clCode[0:2]):
                    #ret.append(i[1])
                    print(i[1])
                elif(len(i[1])!=3):
                    print(i[1])
                    #ret.append(i[1])
                

def findMost(per1):
    largest = []
    largestP = ""
    checked = []
    for x in range(0,10):
            for z in range(0,5):
                if(per1[len(per1)-2][x][z] != "STUDYPD" and (per1[len(per1)-2][x][z] in checked) == False):
                    chk = per1[len(per1)-2][x][z]
                    if(len(per1[len(per1)-2][x][z]) == 2):
                        chk = per1[len(per1)-2][x][z][0]
                    for o in classListNoPrint(per1[len(per1)-2][x][z]):
                        if(o!=per1 and len(o[1]) == len(per1[1])):
                            cur = matchPeriodsNoPrint(per1,o)
                            #print(o[1])
                            if(cur != None):
                             if(len(cur)>len(largest)):
                                largest = cur
                                largestP = o
                    checked.append(per1[len(per1)-2][x][z])
                    print(checked)
    matchPeriods(per1,largestP)
    print(largestP[1])
    return largestP
                    #print("Week " + str((x//5)+1) + "| "+wkNumToEng(x-((x//5)*5)) + "#  | Period " + str(z+1),per2[len(per2)-2][x][z])


    
def timeTablelist(pr):
    if(len(pr[len(pr)-2]) == 10):
        print("MON       TUE       WED       THU       FRI       MO2       TU2       WE2       TH2       FR2")
        print("---------------------------------------------------------------------------------------------")
        for x in range(0,5):
                for z in range(0,10):
                  if(len(pr[len(pr)-2][z][x])==2):
                      print(pr[len(pr)-2][z][x][0],end=" | ")
                  else:
                      print(pr[len(pr)-2][z][x],end=" | ")
                print("\n")



def getCurrentPeriod(period,day,week,lesson,year):
    day = ((week-1)*5) + (day-1)
    print(day,period)
    if(lesson=="STUDYPD"):
        for i in data:
            try:
             if(len(i[len(i)-2]) == 10):
                  #print(i[5][day])
                  if(int(i[1][0])>11):
                    if(lesson in i[5][day][period-1] or lesson in i[5][day][period-1][0]):
                        if(year !=0):
                            if(int(i[1][0]) == year):
                                print(i[1])
                        else:
                            print(i[1])
            except:
                pass
                #print("error")
    else:
        for i in data:
            try:
             if(len(i[len(i)-2]) == 10):
                #print(i[5][day])
                if(lesson in i[5][day][period-1] or lesson in i[5][day][period-1][0]):
                    if(year !=0):
                            if(int(i[1][0]) == year):
                                print(i[1])
                    else:
                            print(i[1])
            except:
                pass
    #print(data[3200][1][0])
        
    


def getHomework(pr):
    #index 4
    try:
        c = Calendar(urlopen(pr[4]).read().decode('iso-8859-1'))
        hw = []
        for evn in c.events:
            hw.append(evn)
            print(evn.name+"\n"+evn.description.encode('iso-8859-1').decode('utf-8').replace("<p>","").replace("</p>","").replace("\n","")+"\n")
        if(len(hw)==0):
            print("No homework left.")
    except:
        print("FAILED TO CONNECT.",pr[4])


#findMost(getData("",None))
#print(getData("",None))

#getCurrentPeriod(4,2,2,"STUDYPD",12)
#getHomework(getData("Morrison",None))
#timeTablelist(getData("Vijay",None))
#matchPeriods(getData("Natalie KAinz",None),getData("Vaibhav",None))
#print(getData("Adrian CHOW",None))
classList("12EU506")

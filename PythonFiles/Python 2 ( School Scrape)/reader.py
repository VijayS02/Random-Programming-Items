import arrow
from datetime import datetime
from pytz import UTC # timezone
from ics import Calendar,Event
from urllib.request import urlopen

file = open("data.txt")
data = file.read()
file.close()
data = data.split("\n")
for i in range(0,len(data)):
    temp = data[i].split(",")
    if("[" in temp[1]):
        brak = temp[1][temp[1].index("["):len(temp[1])-1]
        udat = []
        if( "R" in brak or "N" in brak or "C" in brak or "U" in brak):
            
            brak = brak.replace("]","")
            udat.append(brak[1:3])
            udat.append(brak[3:len(brak)])
            udat.append(temp[1][0:temp[1].index("[")])
            temp[1] = udat
    data[i] = temp

"""

url = "https://lionel2.kgv.edu.hk/local/mis/calendar/timetable.php/6590/413d9a4e0e82871228baee5160e55bf0.ics"
typ = input("t/s\n")
name = input("NAME\n")
possible = []
for i in data:
    if((typ == "t") or (typ == "s" and len(i[1]) == 3)):
        if(typ == "s"):
         if(name.lower() in i[1][2].lower()):
            print(i)
            possible.append(i)

        elif(typ=="t" and type(i[1]) == str):
          if(name.lower() in i[1].lower()):
            print(i)
            possible.append(i)

if(len(possible)>1):
             url = possible[int(input("Which one?\n"))-1][3]
elif(len(possible)!=0): 
    url = possible[0][3]

"""
def getDat(url):

    c = Calendar(urlopen(url).read().decode('iso-8859-1'))
    weeks = []


    for evn in c.events:
        curv = evn.begin.to('local')
        
        if(curv.format("YYYY") == "2018" and curv.format("MM") == "11" and int(curv.format("DD")) >=5 and  int(curv.format("DD")) <=16):
           weeks.append(evn)
    weeks = weeks[::-1]
    for i in weeks:
        print(i.name,i.begin.to('local').format("YYYY-MM-DD HH:mm"))
        curv = i.begin.to('local')
        if(curv.format("HH:mm") == "15:20"):
                    weeks.pop(weeks.index(i))

    if(len(weeks)!= 0):
        match = ["08:15","09:25","11:15","12:25","14:20"]*10
        dat = []
        #print(len(match),len(weeks))
        tmp = []
        lessons = []
        for i in range(0,len(match)):
            
            if(i%5==0 and i!=0):
                dat.append(tmp)
                tmp = []
                
            try:
                
                #print(i)
                curv = weeks[i].begin.to('local')
                if(curv.format("HH:mm") == "15:20"):
                    pass
                elif(curv.format("HH:mm") != match[i]):
                    prd = arrow.get((curv.format("YYYY-MM-DD ") + match[i]),"YYYY-MM-DD HH:mm").replace(tzinfo='local')
                    #print(prd)
                    nxt = prd.replace(hours=+1)
                    e = Event("Study Period",prd,nxt,None,None,"STUDYPD")
                    weeks.insert(i,e)
                    #print(i,len(weeks),curv.format("HH:mm"),match[i])
                    i= i-1
                    tmp.append(e)
                    
                #print(i,len(weeks),weeks[i],match[i])
                else:
                    tmp.append(weeks[i])
                if(weeks[i].name != "Study Period" and (weeks[i].name in lessons) == False):
                        lessons.append(weeks[i].name)
            except IndexError:
                prd = arrow.get((curv.format("YYYY-MM-DD ") + match[i]),"YYYY-MM-DD HH:mm").replace(tzinfo='local')
                #print(prd)
                nxt = prd.replace(hours=+1)
                e = Event("Study Period",prd,nxt,None,None,"STUDYP")
                weeks.insert(i,e)
                tmp.append(e)
                if(weeks[i].name != "Study Period" and (weeks[i].name in lessons) == False):
                    lessons.append(weeks[i].name)
                #print(i,len(weeks),curv.format("HH:mm"),match[i])   
                break
            #print(i,len(weeks),curv.format("HH:mm"),match[i])   
                
            #print(curv.format("HH:mm"))
            #prev = curv.format("HH:mm")
            

        dat.append(tmp)
        final = []
        #print(lessons)
        for i in dat:
            tmp = []
            for z in i:
                tmp.append(z.description)
            final.append('-'.join(tmp))
        #print(dat[dt-1+weekday][prd].description)
        return '|'.join(final)
    else:
        return ""
nf = open("data2.txt").read()
nf= nf.split("\n")
count = 0 
for i in [data[4400]]:
    if(i[0] != "SID"):
     if(int(i[0])>=7612):
        count = data.index(i)
        #print(count)
        try:
            print(i[1])
            x = getDat(i[3])
            print(x)
            nf[count] = ','.join(nf[count].split(",").pop()) + "," +x
            count+=1
        except:
            print("NOT A URL:" + i[3])


#getDat("https://lionel2.kgv.edu.hk/local/mis/calendar/timetable.php/7606/568bc32db74e401b5b60386dfa3a3e04.ics")
file = open("data2.txt","w")
file.write('\n'.join(nf))
file.close()


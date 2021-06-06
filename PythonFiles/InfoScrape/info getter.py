import copy
file  = open('info1.txt')
raw = file.read()
temp = raw.split('\n')
for item in temp:
    cur = temp.index(item)
    temp[cur] = item.split('|')
    temp[cur][1] = temp[cur][1].split(',')
    for o in temp[cur][1]:
        if(o!="Empty"):
            x = temp[cur][1].index(o)
            temp[cur][1][x] = temp[cur][1][x].split(' ')
rooms = copy.copy(temp)

data = '\t1Mo1\t1Mo2\t1Mo3\t1Mo4\t1Mo5\t1Mo6\t1Tu1\t1Tu2\t1Tu3\t1Tu4\t1Tu5\t1Tu6\t1We1\t1We2\t1We3\t1We4\t1We5\t1We6\t1Th1\t1Th2\t1Th3\t1Th4\t1Th5\t1Th6\t1Fr1\t1Fr2\t1Fr3\t1Fr4\t1Fr5\t1Fr6\t2Mo1\t2Mo2\t2Mo3\t2Mo4\t2Mo5\t2Mo6\t2Tu1\t2Tu2\t2Tu3\t2Tu4\t2Tu5\t2Tu6\t2We1\t2We2\t2We3\t2We4\t2We5\t2We6\t2Th1\t2Th2\t2Th3\t2Th4\t2Th5\t2Th6\t2Fr1\t2Fr2\t2Fr3\t2Fr4\t2Fr5\t2Fr6'
data.split('\t')

file.close()
file2 = open('teachers.txt')
raw2 = file2.read()
raw2 = raw2.replace("<br>",'-')
temp = raw2.split('\n')
for item in temp:
    cur = temp.index(item)
    temp[cur] = item.split(',')
teachers = copy.copy(temp)

def roomfinder(rid,rooms):
    for o in rooms:
        if(o[0] == rid):
            return o


def dayFinder(day,period,week,rooms,room):
    cur = roomfinder(room,rooms)
    add = 0
    if(week == 2):
        add = 7*5
    add = add + (day-1)*5
    add = add + period
    return cur[1][add]

def teachergetter(teachers,pdclass):
    if(pdclass != "Empty"):
        for t in teachers:
            if(t[1] == pdclass[1]):
                return t[0]

print(teachergetter(teachers,dayFinder(4,5,2,rooms,"G2")))

def students():
    file = open('List.txt','r')
    raw1 = file.read()
    file.close()
    raw1 = raw1.split('|')
    for x in range(0,len(raw1)):
        raw = raw1[x].split('\n')
        for i in range(0,len(raw)):
            raw[i] = raw[i].split('\t')[0:5]
            raw[i] = '\t'.join(raw[i])

    raw = '\n'.join(raw)
    raw1[x] = raw
    print(raw1)
    temp = '|'.join(raw1)


    file = open('List.txt','w')
    file.write(temp)
    file.close()

def teachers():
    file = open('teachers.txt', 'r')
    raw1 = file.read()
    file.close()
    raw1 = raw1.split('\n')
    file = open('teachers.txt', 'w')

    for i in range(0,len(raw1)):
        raw1[i] = raw1[i].split(',')
        temp = raw1[i][0]
        raw1[i] = raw1[i][1] + "\t" + raw1[i][0] + "\t" + "00" + "\t" + "N/A" + "\t" + "N/A"+"\n"
        file.write(raw1[i])
    file.close()


teachers()
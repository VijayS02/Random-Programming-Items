while (True):
    val = input()
    temp = []
    for i in range(0,len(val)):
       temp.append( val[len(val)-1-i])

    print(''.join(temp))

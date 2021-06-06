def prb1():
    raw = int(raw_input())
    data = []
    for i in range(0,raw):
        x = int(raw_input())
        if(x != 0):
            data.append(x)
        else:
            try:
                data.pop()
            except:
                print("Out of range.")
    sum = 0
    for i in data:
        sum = sum + i
    print(sum)

#prb1()


def prob2Calc(inpt):
    if(inpt == 'L'):
        return 2
    elif(inpt == 'M'):
        return 1
    elif(inpt == 'S'):
        return 0
def prb2():
    raw = int(raw_input())
    raw2 = int(raw_input())
    data = [[],[]]
    for i in range(0,raw):
        data[0].append(prob2Calc(raw_input()))
    for i in range(0,raw2):
        x = raw_input()
        x= x.split(' ')
        x[0] = prob2Calc(x[0])
        x[1] = int(x[1])
        data[1].append(x)
    print(data)

prb2()
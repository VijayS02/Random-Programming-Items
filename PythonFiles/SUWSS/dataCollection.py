import scipy.io
import numpy as np
import sys
import os.path


import matplotlib.pyplot as plt
trans = [139.62,119.43,36.48,14.5]
mdata = []

def avgWaveSpeed(data,ampStart,ampEnd,freq,transducers,index1,index2):
    total = 0
    count = 0
    print(data)
    zer = highestPoint(data,ampStart,0)[0]
    tz = np.arange(ampStart,ampEnd,(1/freq))
    for i in tz:
        tmp = highestPoint(data,i,zer)
        #print(tmp)
        print(tmp, " " , index1 , " ", index2)
        total = total + (transducers[index2]-transducers[index1])/(tmp[index2+1] -tmp[index1+1])
        count = count +1
    total = total/count
    return abs(total*1000)

def highestPoint(data,val,start):
    x = []
    x.append(0)
    
    for b in range(start,len(data)):
        count = 0
        i = data[b]
        #print(i," ",count)
        for z in i :
            if(z[0] > val):
                x.append(count)
                break
            count = count + 1
        
    lowest = 10000
    highest = 0
    for v in x:
        if(v <= lowest):
            lowest = v 
        if(v>= highest):
            highest = v
    x[0] = lowest
    x.append(highest)
    return x

def cailbration(data):
    high = False
    for x in data:
        if(x[0]>2):
            high = True
            break

    if(high):
        for z in range(0,len(data)):
            data[z] = ((data[z]*0.5001 + 1.0032 - 1.01325)*10.1974)+10
    else:
        for z in range(0,len(data)):
            data[z] = ((data[z]*3.1277 - 0.263 - 1.01325)*10.1974)+10
    return data


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    text = ""
    if(os.path.isfile('testfile.txt')):
        file2 = open('testfile.txt')
        text = file2.read()
        file2.close()
    file = open('testfile.txt',"w")
    file.write(text + str(event.ydata)+'\n')
    file.close()
    mdata = []
    x = open('testfile.txt').read().split('\n')
    if(len(x) >2):
        #print(x)
        mdata.append(float(x[0]))
        mdata.append(float(x[1]))
        file = open('testfile.txt',"w")
        file.write("")
        file.close()
    
    
    #print(avgWaveSpeed(data,mdata[0],mdata[1],10,trans,2,0))
    
    
    
    
def main(file,idx,x):
    fig = plt.figure(x)
    gid = 200+(x*10)+idx
    #if(x==1):
        #fig = plt.figure(3)
    #else:
        #fig = plt.figure(4)
    #location = input('MatLabFile Location\n')
    location = file
    mat = scipy.io.loadmat(location)
    data = []
    x = mat.get('VoltageAI0')[0][0][1][0][0]
    time = []
    for i in range(0,x):
        time.append(i/1000)

    #print(time)
    for i in range(0,10):
        tmp = 'VoltageAI'+str(i)
        if(mat.get(tmp)==None):
            break
        else:
            data.append(cailbration(mat.get(tmp)[0][0][0]))
    colors = ['b','y','m','k','r']
    count = 0
    #zxcv =  avgWaveSpeed(data,29.5,31,10,trans,2,0)
    pltinone = True
    #zxc = input("All in one? y/n?\n")
    zxc = "y"
    if(zxc =="n"):
       pltinone = False
       fig = plt.figure(2)
    for i in data:
        if(pltinone):
            plt.subplot(gid)
            line = plt.plot(time,i)
            import random
            r = lambda: random.randint(0,255)
            colorz = ('#%02X%02X%02X' % (r(),r(),r()))
            plt.setp(line,'color',colorz,'antialiased',True)
        else:
            cur = 221 + count
            plt.subplot(cur)
            plt.ylabel('Bar ( gauge )')
            plt.xlabel('Time ( s )')
            line = plt.plot(time,i)
            plt.setp(line,'color',colors[count],'antialiased',True)
        count = count+1

    plt.ylabel('Meters of water( m )')
    plt.xlabel('Time ( s )')
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.axis([0,8, 25, 35])
    

    fig.canvas.mpl_disconnect(cid)
    #return zxcv
    return 1
sumx = 0
vals = []

main("D:\\Files\\Documents\\Programming\\PythonFiles\\SUWSS\\TDMS\\24July2018_Intact_1.mat",1,1)
#for i in range(1,2):
#   print(i)
#    sumx = sumx+(main('\TDMS\24July2018_Intact_'+str(i)+'.mat',i,2))
#print(sumx)
'''
sumy= 0
i = 6
for i in range(6,11):
    print(i)
    sumy = sumy+(main('LL Pipe Case\\24July2018_LL_'+str(i)+'.mat',240+i-5,2))

sumy = (sumy/5)
'''
#print(abs(sumx-sumy))

plt.show()

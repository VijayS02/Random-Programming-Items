import scipy.io
import scipy.fftpack
import numpy as np
import math
import colorsys
import random
import matplotlib.pyplot as plt

trans = [139.62,119.43,36.48,14.5]
mdata = []


def avgWaveSpeed(data,ampStart,ampEnd,freq,transducers,index1,index2):
    total = 0
    count = 0
    #print(data)
    zer = highestPoint(data,ampStart,0)[0]
    tz = np.arange(ampStart,ampEnd,(1/freq))
    #print(tz)
    for i in tz:
        tmp = highestPoint(data,i,zer)
        #print(tmp)
        #print(tmp, " " , index1 , " ", index2)
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

def getData(file):
    location = file
    mat = scipy.io.loadmat(location)
    data = []
    x = mat.get('VoltageAI0')[0][0][1][0][0]
    for i in range(0,10):
        tmp = 'VoltageAI'+str(i)
        if(mat.get(tmp)==None):
            break
        else:
            data.append(cailbration(mat.get(tmp)[0][0][0]))
    
    return data

def createGraph(gid,grp,inone,freq,tite,hdinfo,culz,time,ax,indx,sz,fig):
    #print(time)
    count = 0
    for vals in grp:
            print(vals)
            if(inone== False):
               # plt.subplots(sz, sz)
                pass
            #print(vals)
            #print("\n")
            line = plt.plot(time,vals)
            plt.legend(['L2','L4','L7','L8'])
            plt.subplot(gid)
            plt.setp(line,'color',culz[count%len(culz)],'antialiased',True,linewidth="1.0")
            plt.ylabel(ax[1][0])
            plt.subplots_adjust(hspace=0.4)
            plt.xlabel(ax[1][1])
            #STARTING AXIS : (XMIN,XMAX,YMIN,YMAX) PRE COMPUTED BY FINDING JAKOWSKY HEAD
            if(ax[0][0] == 0 and ax[0][1] == 0 and ax[0][2] == 0 and ax[0][3] == 0):
                xmin, xmax, ymin, ymax = int(hdinfo[0] / freq) - 1, int(hdinfo[0] / freq) + 3, hdinfo[1] - 4, hdinfo[1] + 0.5
            else:
                xmin, xmax, ymin, ymax = ax[0][0], ax[0][1], ax[0][2], ax[0][3]
                #print(str(xmin)+ " min " + str(xmax) + " max . " +str(ymin)+ " min " + str(ymax) + " max . " )
            plt.axis([xmin,xmax,ymin,ymax])
            plt.title(tite)
            count = count + 1


def plotData(info,inone,freqArr,ttls,hdinfo,cols,time,ax):
    #print(info)
    if(len(info) ==0):
        return

    fls = len(info)
    #print(str(fls) + " is fls")
    x = 1
    if(inone == False):
        #print(math.log(fls,2))
        if(math.log(fls,2) < 1.0):
            x = 1
        else:
            x = int(math.ceil(math.log(fls,2)))
    fig = plt.figure(x)
    sz = int(math.sqrt(fls)+1)

    #fig = plt.subplots(sz,sz)
    gid = 200+(x*10)+1

    #print(str(x) +"  is fgs" )
    indx = 0
    for groups in info:
        createGraph(gid,groups,inone,freqArr[indx],ttls[indx],hdinfo[indx],cols,time[indx],ax[indx],indx,sz,fig)
        if(inone == False):
            gid = gid+1
        if(gid > 200+(x*10)+8):
            gid = gid + 10 - 8
        indx = indx + 1            

    plt.show()



def jhead(pipeThic,pipedi,wavespd,flowrt):

    dia = (pipedi - (2 * pipeThic)) * 0.001
    flwms = flowrt / 1000
    area = math.pi * ((dia / 2) ** 2)

    final = 1000 * wavespd * ((flwms) / area) * 0.00010199773339984
    return final



def fft(data,freq):
    datanew = []
    for i in range(0,len(data)):
        datanew.append(data[i][0])
    #print(datanew)
    data = datanew
    # Number of samplepoints
    N = len(data)
    # sample spacing
    T = 1.0 / freq
    #x = np.linspace(0.0, N * T, N)
    y = data
    #y = np.sin(5.0 * 2.0 * np.pi * x) + 0.5 * np.sin(2.0 * 2.0 * np.pi * x)
    #print(y)
    #Mean removed from each value
    ke = np.mean(y)
    for i in range(0,len(y)):
        y[i] = y[i]-ke
    #yf = fft of data minus the mean of the entire array
    yf = scipy.fftpack.fft(y)
    #xf = np.linspace(0.0,1/T-(1/T)/N, N)
    xf = np.arange(0,(((freq-freq/N)+1/freq)/2) - 1/freq,freq/(N))
    #print(xf)
    #np.abs = absolute value
    #print(np.abs(yf)[:(N//2)])
    return [np.abs(yf)[:(N//2)],xf]

def getHeadLoc(wvSpd,dat):
    pipe_Thickness = 8
    pipe_Diameter = 90
    waveSpeed = wvSpd
    flow_rate = 0.47
    inf = jhead(pipe_Thickness, pipe_Diameter, waveSpeed, flow_rate)
    normal = np.mean(dat[0][0:1000])
    search = normal + inf - 0.5
    print("Approx calculated pressure point for Jhead: "+ str(search))
    return [highestPoint(dat,search,0)[1],search+0.5]



"""
Calls the jhead function that calculates the Jakowsky head Delta P with given parameters
The variables declare the values for each parameter e.g. pipe thickness = thickness of pipe (mm)
"""

pipe_Thickness = 8
pipe_Diameter = 90
waveSpeed = 353.8743
flow_rate = 0.47
#print(jhead(pipe_Thickness,pipe_Diameter,waveSpeed,flow_rate))
colors = [[230, 25, 75],[60, 180, 75],[255, 225, 25],[0, 130, 200],[245, 130, 48],[145, 30, 180],[70, 240, 240],[240, 50, 230],[210, 245, 60],[250, 190, 190],[0, 128, 128],[230, 190, 255],[170, 110, 40],[255, 250, 200],[128, 0, 0]]
for i in range(0,len(colors)):
    for rgb in range(0,len(colors[i])):
        colors[i][rgb]= colors[i][rgb]/256
#print(colors)
data = []
frq = []
titles = []
time = []
ax = []
searchRange = [[37,38],[40,41],[40,41],[40,41],[40,41],[40,41]]
#searchRange = [[38,39],[38,39],[38,39],[38,39],[38,39],[38,39]]
jheadinfo = []
freq = 1000
for i in range(1,6):
    temp = getData('D:\\Files\\Documents\\Programming\\PythonFiles\\SUWSS\\24July2018_Waqar\\Intact Pipe Case\\24July2018_Intact_'+str(i)+'.mat')
    #temp.pop(2)
    data.append(temp)
    frq.append(freq)

    time.append(np.arange(0,len(temp[0])/freq,1/freq))
    ax.append([[0,0,0,0],["Meters","Time (s)"]])
    wvspd = avgWaveSpeed(temp,searchRange[i][0],searchRange[i][1],100,trans,0,2)
    print("Calculted approx wavespeed: " + str(wvspd))
    jheadinfo.append(getHeadLoc(wvspd,temp))
    #jheadinfo.append([0,0])
    titles.append('Test: ' + str(i) )


data2 = []
frq2 = []
titles2 = []
time2 = []
ax2 = []
jheadinfo2 = []
for i in range(0,5):
    cur = []
    timetmp = 0
    for z in data[i]:
        tmp = fft(z,frq[i])
        cur.append(tmp[0])
        timetmp = tmp[1]
    time2.append(timetmp)
    frq2.append(freq)
    data2.append(cur)
    titles2.append("FFT of Test: " +str(i))
    jheadinfo2.append(jheadinfo[i])
    ax2.append([[-5,20,0,1500],["M/hz Frequency","Frequency (hz)"]])


titles.append("Sup")
frq.append(1000)


#n = len(data[0])



#data.append(fft(data[0][0][jheadinfo[0][0]:len(data[0][1])],1000))
#titles.append("")
#print(time)
#plotData(data,False,frq,titles,jheadinfo,colors,time,ax)
#plotData(data2,False,frq2,titles2,jheadinfo2,colors,time2,ax2)

#data.append(getData('D:\\Files\\Documents\\Programming\\PythonFiles\\SUWSS\\TDMS\\24July2018_Intact_1.mat'))
#for i in range(0,len(data[0])):
    #data[0][i] = data[0][i][16000:len(data[0][i])]

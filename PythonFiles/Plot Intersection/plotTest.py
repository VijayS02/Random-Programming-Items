import matplotlib.pyplot as plt
import numpy as np
def intersect(x1,y1,x2,y2):
    intersections = []
    if(len(x1)>len(x2)):
        max = len(x2)
    else:
        max = len(x1)
    for i in range(max):
        if(x1[i] == x2[i] and y1[i] == y2[i]):
            intersections.append(i)
    
    return intersections


c=50
sideMove = 20

demand = [[np.arange(0+c,100+c,1),np.arange(100+c+sideMove,0+c+sideMove,-1)]]
supply = [[np.arange(0+c,100+c,1),np.arange(0+c,100+c,1)]]


x = demand[0][0]
y = demand[0][1]
x1 = supply[0][0]
y1 = supply[0][1]
v = intersect(x,y,x1,y1)
comx = []
comy = []
for z in v:
    comx.append(x[z])
    comy.append(y[z])
    plt.plot([x[z], x[z]], [-10, y[z]], 'k-',dashes=[2, 2])
    plt.plot([-10, x[z]], [y[z], y[z]], 'k-',dashes=[2, 2])

print(comx,comy)
plt.plot(x1,y1)
plt.ylabel("Price ($)")
plt.xlabel("Quantity")
plt1, = plt.plot(x,y,label="Supply")
plt.legend(handles=[plt1])
plt.plot(comx,comy,'ro')
plt.axis([0,200,0,200])
plt.show()


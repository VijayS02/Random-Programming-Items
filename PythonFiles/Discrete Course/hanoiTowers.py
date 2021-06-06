import numpy as np
def move(dat,i,x,n,count):
    print(x, "",i,"N:",n, dat)
    if(n==1):
        dat[x].append(dat[i].pop())
        count += 1
    else:
        count = move(dat,i,getother(x,i),n-1,count)
        dat[x].append(dat[i].pop())
        count +=1
        count = move(dat, getother(x, i),x , n-1, count)
    print(x, "",i,"N:",n, dat)
    return count

def getother(x,i):
    if((x ==0 or i ==0)):
        if( ((x==2 or i==2)==False)):
            x +=1
        else:
            x+=2
    return (x+i) % 3

sizeofarr = 4

data = [np.arange(sizeofarr,0 , -1).tolist(),[],[]]
print(move(data,0,2,sizeofarr,0))
print(data)

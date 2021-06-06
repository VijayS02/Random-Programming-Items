def runthing(num):
    count =0
    while True:
        if(num==1):
            return count+1
        if(num%2==0):
            num = num/2
            count= count+1
        else:
            num = (3*num) + 1
            count = count + 1


for i in range(0,10000):
    runthing(i)
print(runthing(13))
        

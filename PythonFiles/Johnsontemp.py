'''
userint = int(input('Enter a number and I will list out all the divisors'))
listn=[]

for x in range(1,userint+1):
    if userint%x == 0:
        listn. append(x)
    
        
print(listn)
'''
'''
a =[]
b=[]

done=False

while not done:
    c= input('Enter a number for list 1,enter 01 to quit')
    if c == '01':
        done = True

    else:
        a.append(int(c))
        done=False
a.sort()

done=False
while not done:
    d= input('Enter a number for list 2,enter 01 to quit')
    if d == '01':
        done = True

    else:
        b.append(int(d))
        done=False
b.sort()

amper=[]
same= True
last =0
for value in a:
    if( value in b and value != last):
        amper.append(value)
        last = value
        
print(amper)

'''
palinlist =[]


done=False

while not done:
    c= input('Enter a string,enter 01 to quit')
    if c == '01':
        done = True

    else:
        palinlist.append(c)
        done=False


goodboi= palinlist[::-1]

if palinlist == goodboi:
    print('its a Palindome')
else:
    print('its not')
        
        

        



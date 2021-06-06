import random as rand
for i in range(0,10):
      x = input("Stone paper or sis no caps?\n")
      lst = ['stone','paper','sis']
      y = rand.randrange(0,3)
      temp = lst.index(x.replace(' ',''))-1
      if(temp == -1):
          temp = 2
      print(temp)

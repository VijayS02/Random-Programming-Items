class Usage:
    def __init__(self,bikeInfo):
        bikeInfo = bikeInfo.split(',')
        self.bike = int(bikeInfo[0])
        self.uses = int(bikeInfo[1])
        self.returned = bikeInfo[2]
    def add(self):
        self.uses = self.uses - 1

fl = file.open('x.txt','r')
data = fl.read()
data = data.split('\n')
for i in data:
    data[data.index(i)] = i.split(',')
    
bike1 = Usage(data[0])
bike2 = Usage(data[1])
print(bike1.uses)
bike1.add()
print(bike1.uses)

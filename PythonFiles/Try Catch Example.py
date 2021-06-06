def validation(inptStr):
 while True:
    try:
        inptStr = int(inptStr)
        if(inptStr>=0 and inptStr <= 100):
            break
        else:
            print("Out of range.\n")
            inptStr = validation(input(""))
    except:
        print("jews are gay")
        inptStr = validation(input(""))
 return inptStr

scores = []
for i in range(0,5):
    print("Enter score for test",i+1,'.')
    scores.append(validation(input('')))

print(scores)
print(scores[1])

remove = False
raw = list(input(""))
removal = []
for i in range(0,len(raw)):
    cur = raw[i]
    if(cur == "("):
        remove = True
    elif( cur == ")"):
        remove = False

    if(remove == True):
        raw[i] = ""

print(''.join(raw).replace(")",""))

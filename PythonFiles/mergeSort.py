import random
import time

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array

def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c



def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

def listGen(size,numbRange):
    lst = []
    for i in range(0,size):
        lst.append(random.randrange(0,numbRange))
    return lst



while True:
    lstSize = int(raw_input("What size list?\n"))
    xrange = int(raw_input("What number range?\n"))
    list = listGen(lstSize,xrange)
    print('LIST (first 5): ',list[0:5])
    start_time = time.time()
    listx = (quicksort(list))
    print("--- %s Quick seconds ---" % (time.time() - start_time))
    print('LIST SORTED (first 5): ', listx[0:5])
    start_time = time.time()
    listx = list
    listx.sort()
    print("--- %s Python Sort seconds ---" % (time.time() - start_time))
    print('LIST SORTED (first 5): ', listx[0:5])
    if(raw_input("One more?").lower() != 'y'):
        break

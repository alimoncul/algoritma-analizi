import random
import time

def recursive_fib(n):
    if(n<2):
        return n
    else:
        return recursive_fib(n-1)+recursive_fib(n-2)

def generateList(n):
    baslangic=time.time()
    newList=[]
    for i in range(n):
        newList.append(random.randint(0,100000000))
    bitis=time.time()
    print("zaman: ",bitis-baslangic)
    return newList

def myf(myList):
    baslangic=time.time()
    max=myList[0]
    s=-1
    for i in range(len(myList)):
        if(max<=myList[i]):
            max=myList[i]
            s=i
    bitis=time.time()
    print("zaman: ",bitis-baslangic)
    return max,s

#list_1=generateList(10000000)
#myf(list_1)
baslangic=time.time()
recursive_fib(41)
bitis=time.time()
print("zaman: ",bitis-baslangic)
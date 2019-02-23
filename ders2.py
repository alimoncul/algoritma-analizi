def BinarySearch(liste,element):
    bas = 0
    son = len(liste) - 1

    while bas <= son:
        orta = int((bas + son) / 2)
        if (liste[orta] == element):
            return element," sayısı listede mevcut ve index'i: ",orta
        elif (liste[orta] > element):
            son = orta - 1
        elif (liste[orta] < element):
            bas = orta + 1
        else:
            return "eleman yok"

def call_report_recursive(x,y):
    global sayac
    sayac=0
    r=power_recursive(x,y)
    print(x," üzeri ",y," degeri: ",r," çağrım sayısı: ",sayac)

def power(x,y):
    t=1
    for i in range(y):
        t=t*x
    return t

sayac=0
def power_recursive(x,y):
    global sayac
    sayac=sayac+1
    if(y==0): return 1
    elif(y==1): return x
    elif(y%2==0): return power_recursive(x*x,int(y/2))       
    elif(y%2==1): return power_recursive(x*x,int(y/2))*2

def SelectionSort(liste):
    for element in range(len(liste)-1,0,-1):
        positionOfMax=0
        for location in range(1,element+1):
            if(liste[location]>liste[positionOfMax]):
                positionOfMax=location
        trade=liste[element]
        liste[element]=liste[positionOfMax]
        liste[positionOfMax]=trade
    return liste
    
#print(SelectionSort([93,42,56,67,643,235,654,87,99]))
#print(power_recursive(2,8))
#print(power(2,8))
#print(call_report_recursive(2,8))
#print(BinarySearch((3,5,12,43,53,88,95),43))





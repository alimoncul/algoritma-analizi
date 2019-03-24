# coding: utf-8

# In[15]:

def rec_fb(n, result):
    if n<2:
        return n
    elif(result[n]!=0):
        return result[n]
    else:
        result[n] = rec_fb(n-1,result) + rec_fb(n-2,result)
        return result[n]
    
def recMC(coinValueList, change, knownResults):
    minCoins = change
    if (change in coinValueList):
        knownResults[change]=1
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList,change-i,knownResults)
            if (numCoins < minCoins):
                minCoins = numCoins
                knownResults[change]=minCoins
    return minCoins

for i in range(13,50):
    print(rec_fb(i,[0]*(i+1)),end=" ")

for i in range(13,200):
    print(i," ",recMC([1,5,10,25,50],i,[0]*(i+1)))


# In[ ]:

# coding: utf-8

# In[10]:

# matrix_1 MxN
# matrix_2 NxP
# matrix_3 = matrix_1 * matrix_2

def multiplyMatrix(matrixA,matrixB): #O(n^3)
    if(len(matrixA[0])!=len(matrixB)):
        return "Boyutlar uyumsuz"
    else:
        r=[]
        for i in range(len(matrixA)):
            r.append([])
            for j in range(len(matrixB)):
                a=getRowFromMatrix(matrixA,i)
                b=getColFromMatrix(matrixB,j)
                c=getValueFromRowCol(a,b)
                r[i].append(c) 
        return r
    

def getValueFromRowCol(row,col): #O(n)
    sumMultiplication=0
    for i in range(len(row)):
        sumMultiplication=sumMultiplication+row[i]*col[i]
    return sumMultiplication

def getRowFromMatrix(matrix,i):
    return a[i]
 
def getColFromMatrix(matrix,i):
    return [row[i] for row in matrix]

a=[[1,2],[3,5],[12,41]]
b=[[45,2354,234,523],[67,8,6,56]]
c=multiplyMatrix(a,b)
print(c)




    


# In[ ]:




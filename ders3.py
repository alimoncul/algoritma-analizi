import ctypes
from pympler import asizeof

#dynamicarray yapısı karmaşıklıgı nedir? Hangi durumlarda O(n) olur?
class DynamicArray:
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k <self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity: #kapasite yeterli degilse, kapasiteyi 2'ye katla.
            print("Array kapasitesi yeterli değil! Kapasite arttırılıyor.")
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1
        
    def _resize(self, c): 
        B = self._make_array(c) 
        for k in range(self._n): 
            B[k] = self._A[k]
        self._A=B 
        self._capacity = c
        
    def _make_array(self, c): 
        return(c*ctypes.py_object)()
    
    def getsize(self):
        import sys
        return sys.getsizeof(self._A)
    
    def getLength(self):
        return len(self._A)
    
myArray = DynamicArray()
for i in range(512):
    myArray.append(i)
    print(i," eklendi. ---> Array size: ",myArray.__len__()," Array Length: ",myArray.getLength())


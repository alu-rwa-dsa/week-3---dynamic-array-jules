import ctypes


class Array():

    arr = []

    def __init__(self):
        self.n = 0 
        self.capacity = 1   
        self.A = self._array(self.c)
        self.__class__.arr_list.append(self)

    def len(self):
      
        return self.n

    def get(self, i):
       
        if not 0 <= i < self.n:
            
            return IndexError('i is out of bounds !')

        return self.A[i]   

    def set(self, val, i):
        
        if i < 0 or i > self.n:
            print("please enter index")
            return

        if self.n == self.c:
            self.resize(2*self.c)
  
        for j in range(self.n - 1, i - 1, - 1):
            self.A[j+1] = self.A[j]

        self.A[i] = val
        self.n += 1
    
    def resize(self, nw_cap): 
     
        
        B = self._array(nw_cap) 

        for k in range(self.n): 
            B[k] = self.A[k]
              
        self.A = B 
        self.capacity = nw_cap 
          
    def _array(self, nw_cap): 
       
        return (nw_cap * ctypes.py_object)()


class DynamicArray(Array):

    def add(self, val):
        
        if self.n == self.c:
            
            self.resize(2 * self.capacity)  
    
        self.A[self.n] = val  
        self.n += 1

    def delete(self):
        

        if self.n == 0:
            print("Array is empty deletion not Possible")
            return

        self.A[self.n - 1] = 0

        self.n -= 1


if __name__ == "__main__":
    array_1 = Array()

    array_1.__set__(45, 0)
    array_1.__set__(34, 0)

    print(array_1.__len__())

    arrayDynamic = DynamicArray()

    arrayDynamic.add(57)
    arrayDynamic.add(37)

    arrayDynamic.delete()
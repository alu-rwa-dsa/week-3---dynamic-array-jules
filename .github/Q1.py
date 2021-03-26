import ctypes
import gc


class Array():

    arr_list = []

    def __init__(self):
        self.n = 0 
        self.c= 1   
        self.A = self.make_array(self.c)
        self.__class__.arr_list.append(self)

    def len(self):
        
        return self.n

    def get(self, i):
       
        if not 0 <= i < self.n:
            
            return IndexError('i is out of bounds !')

        return self.A[i]   
    def set(self, val, i):
      
        if i < 0 or i > self.n:
            print("please enter an index")
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
            self.A = B 
            self.c = nw_cap 
          
    def _array(self, nw_cap): 
        
        return (nw_cap * ctypes.py_object)()

    
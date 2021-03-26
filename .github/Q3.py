

def MergelinkedList(list):
    ls = []
    for l in ls:
        ls.extend(l)
        r= set(ls)
        l = list(r)

    return l


if __name__ == "__main__":
    a = [[2, 4, 9, 2, 1, 6], [9, 5, 22, 1, 0, 56, 8, 5]]

    print(MergelinkedList(a))

import ctypes
import gc


from q2 import DynamicArray, Array


class Darray(DynamicArray, Array):

    def __init__(self, array):
        DynamicArray.__init__(self, array)    
        Array.__init__(self, array)
        self.array = array

    def contains(self, var):
        e = var in self.array
        return e
        
    def reverse(self):
        reverse_arr = self.array[::-1]
        return reverse_arr

    def set(self, var, i):
        return self.array[:i] + [var] + self.array[i:]


    # Space Complexity: O(1)
    # Time Complexity: O(1)

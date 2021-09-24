"""
The constructor is taking non-zero values into a dictionary, 
so it is O(n) time. 

And dotProduct() is just 
looping over one dictionary 
against the other dictionary, 

multiply and sum up. 

For the follow up question, 
the one dictionary with shorter length 
is selected as the driver for the loop in dotProduct() 
so time is O(len(shorter dictionary))
"""

class SparseVector:
    def __init__(self, nums):
        self.d = {i:val for i, val in enumerate(nums) if val != 0}
 
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        if len(self.d) <= len(vec.d):
            A, B = self.d, vec.d
        else:
            A, B = vec.d, self.d
            
        for i, val in A.items():
            res += val*B.get(i,0)
        return res
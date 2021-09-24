import math
import collections

# O(N**0.5)
def shiftArray(arr1, arr2):
    n = len(arr1)
    m = math.ceil(n ** 0.5)

    dic = collections.defaultdict(int)
    for i in range(m):
        dic[arr1[i]] = i
    
    for k, v in dic.items():
        if v * m < n and arr2[v * m] in dic:
            return  v  * m - dic[arr2[v * m]]


arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr2 = [5, 4, 3, 2, 1, 9, 8, 7, 6]

# arr1 = [1, 3, 4, 5, 2]
# arr2 = [4, 5, 2, 1, 3]

res = shiftArray(arr1, arr2)
print(res)
            



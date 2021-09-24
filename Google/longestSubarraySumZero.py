def longestSubarraySumZero(arr):
    presums = [arr[0]] * len(arr)
    for i in range(1, len(arr)):
        presums[i] = presums[i-1] + arr[i]
    print(presums)
    dic = {}
    res = 0
    for i, v in enumerate(presums):
        if v == 0:
            res = max(i + 1, res)
        if v in dic:
            res = max((i - dic[v] + 1), res)
        dic[v] = i
    return res

print(longestSubarraySumZero([0, 0, 0, 0]))
    

    

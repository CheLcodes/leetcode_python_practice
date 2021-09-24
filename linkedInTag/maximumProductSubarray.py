"""
求积就比较麻烦了，因为某个位置可能出现了0或者负数。。
当遇到0的时候，整个乘积会变成0；
当遇到负数的时候，当前的最大乘积会变成最小乘积，最小乘积会变成最大乘积。

有上面的分析可以看出，必须使用两个数组分别记录以某个位置i结尾的时候的最大乘积和最小乘积了。
令最大乘积为f，最小乘积为g。那么有：

当前的最大值等于已知的最大值*当前值，最小值*当前值，当前值，这三个数的最大值。
当前的最小值等于已知的最大值*当前值，最小值*当前值，当前值，这三个数的最小值。
结果是最大值数组中的最大值。
时间复杂度是O(N)，空间复杂度是O(N).
"""

class Solution:
    def maxProduct(self, nums) -> int:
        # minp[i]: min product subarray till i
        # maxp[i]: max product subarray till i        
        
        minp = [0] * len(nums)
        maxp = [0] * len(nums)
        
        minp[0] = maxp[0] = res = nums[0]
        
        for i in range(1, len(nums)):
            minp[i] = min(minp[i-1] * nums[i], nums[i], maxp[i-1] * nums[i])
            maxp[i] = max(minp[i-1] * nums[i], nums[i], maxp[i-1] * nums[i])
            res = max(res, maxp[i])
        return res
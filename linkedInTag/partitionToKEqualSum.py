class Solution:
    def canPartitionKSubsets(self, nums, k) -> bool:
        if not nums or len(nums) < k:
            return False
        sums = sum(nums)
        div, mod = sums // k, sums % k
        if mod: return False
        target = [div] * k
        
        return self.backtrack(nums, 0, k, target)
        
        
    def backtrack(self, nums, idx, k, target):
        # used all the nums, divided into k subsets
        if idx == len(nums):
            return True
        num = nums[idx]
        for i in range(k):
            # if target[i] >= num:
            target[i] -= num
            if self.backtrack(nums, idx + 1, k, target):
                return True
            target[i] += num
        return False
    
sol = Solution()
res = sol.canPartitionKSubsets([1, -1, 2, 4, 8, -2, 0, 6], 3)
print(res)
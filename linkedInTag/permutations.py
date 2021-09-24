class Solution:
    def permute(self, nums):
        if not nums:
            return []
        self.res = []
        self.vis = [False] * len(nums)
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        if len(path) == len(nums):
            self.res.append(path)
        for i in range(len(nums)):
            if not self.vis[i]:
                self.vis[i] = True
                self.dfs(nums, path + [nums[i]])
                self.vis[i] = False

sol = Solution()

res = sol.permute([1, 2, 3])
print('res', res)
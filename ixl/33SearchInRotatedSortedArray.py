class Solution:
    @classmethod
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] < target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
             
if __name__ == "__main__":
    
    res = Solution.search([4,5,6,7,0,1,2], 0)
    print('here is the answer', res)



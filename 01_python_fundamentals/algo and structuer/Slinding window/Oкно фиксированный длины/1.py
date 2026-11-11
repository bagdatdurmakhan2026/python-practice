class Solution(object):
    def ans(self, nums, k):
        res = 0
        n = len(nums)
        for i in range(k):
            res+=nums[i]
        mx = res
        for r in range(k, n):
            l = r - k
            res = res + nums[r]-nums[l]
            mx = max(mx, res)
        return mx
      
nums = [3,2,0,9,1,2,8,5,2]
k = 5
print(Solution().ans(nums,k))

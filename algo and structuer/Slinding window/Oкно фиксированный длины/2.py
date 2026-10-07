class Solution(object):
    def res(self, nums, k):
        ans = 0 
        n = len(nums)
        for i in range(k):
            ans += nums[i]**2
        mx = ans
        for r in range(k, n):
            l = r - k
            ans = ans + nums[r]**2 - nums[l]**2
            mx = max(mx, ans)
        return mx
            
    
    
nums = [3, 0, 5, 9,4,1]
k = 3
print(Solution().res(nums,k))
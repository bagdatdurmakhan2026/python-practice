class Solution(object):
    def ans(self, nums):
        l = 0 
        r = 0
        n = len(nums)
        arr = []
        while r < n:
            while r + 1 < n and nums[r]+1 == nums[r+1]:
                r+=1
            if l!=r:
                arr.append(f'{nums[l]}->{nums[r]}')
            else:
                arr.append(f'{nums[l]}')
            r+=1
            l = r
        return arr       
nums = [1,2,3,5,8,9,10]
print(Solution().ans(nums))
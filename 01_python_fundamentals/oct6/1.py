class Solution(object):
    def res(self, n, nums):
        l = 0
        r = 0
        mx = 0
        for i in nums:
            new_l = max(l, r + i)
            new_r = max(r, l - i)  
            l  = new_l
            r = new_r   
        return l

n = input()
nums = [int(x) for x in input().split()]
print(Solution().res(n, nums))
class Solution(object):
    def ans(self, chars,k):
        l = 0
        r = -1 
        result = 0
        n = len(chars)
        take = 0
        while l < n:
            while r + 1 < n and (chars[r+1]== 0 or take < k):
                #if chars[r]
chars = "aabacbebebe"
k = 3
print(Solution().ans(chars, k))
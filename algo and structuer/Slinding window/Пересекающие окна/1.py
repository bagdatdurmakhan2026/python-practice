class Solution(object):
    def res(self, nums,k):
        l = 0
        r = -1 
        n = len(nums)
        answer = 0
        zerocnt = 0
        while l < n:
            while r + 1 < n and (nums[r+1] ==1 or zerocnt<k):
                if nums[r+1]==0:
                    zerocnt+=1
                r+=1
            answer = max(answer, r-l+1)
            if nums[l]==0:
                zerocnt-=1
            l+=1                                                                  
        return answer
nums = [1,0,1,0,1,0,1,1]
k = 2
print(Solution().res(nums,k))
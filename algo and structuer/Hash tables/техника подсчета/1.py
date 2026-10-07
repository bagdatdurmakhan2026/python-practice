class Solution(object):
    def res(self, chars):
        cnt = {}
        for i in chars:
            cnt[i] = cnt.get(i,0)+1
        odd_cnt = 0
        for j in cnt.values():
            if j %2 == 1:
                odd_cnt+=1
        return odd_cnt<=1
            
        
        
chars = "ABC"
print(Solution().res(chars))
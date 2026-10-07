class Solution(object):
    def res(self, a, b):
        check= {}
        cnt = {}
        for i in a: 
            check[i] = check.get(i,0)+1
        for j in b:
            cnt[j] = cnt.get(j,0)+1
        return cnt == check    
a = "ABCC"
b = "CBC"
print(Solution().res(a,b))
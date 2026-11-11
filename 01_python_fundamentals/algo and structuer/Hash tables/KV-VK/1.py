class Solution(object):
    def ans(self, s):
        cnt = {}
        for i in s:
            cnt[i] = cnt.get(i,0) + 1
        arr = [[] for _ in range(len(s)+1)]
        for i, j in cnt.items():
            arr[j].append(i)
        res = []
        for j in range(len(arr)-1,0,-1):
            for i in arr[j]:
                res.append(i*j)
        return "".join(res)        
        
s = "BABBCBC"
print(Solution().ans(s))
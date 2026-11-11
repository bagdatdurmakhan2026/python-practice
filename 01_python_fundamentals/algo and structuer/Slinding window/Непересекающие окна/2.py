class Solution(object):
    def ans(self, chars):
        l = 0
        r = 0
        n = len(chars)
        arr = []
        cnt = 0
        while r < n:
            while r+1 < n and chars[r+1] == chars[r]+1:
                r+=1
                cnt +=r
            if l!=r:
                arr.append(f'{chars[l]}, {cnt}')     
chars = ["x", "x", "y", "z", "z", "z"]
print(Solution().res(chars))
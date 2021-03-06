class Solution:
    def findNth(self,N):
        result = 0
        base = 1

        while N > 0:
            print('num: ', N)
            result += base*(N % 9)
            N = N // 9
            base = base * 10
            print(result)
        return result

            
obj = Solution()
res = obj.findNth(100)
print(res)

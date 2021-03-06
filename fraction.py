"""
Given a positive integer N, the task is to find the Nth natural number after removing all the natural numbers containing digit 9.
"""

class Solution:
    def findNth(self,N):
        result = 0
        base = 1

        while N > 0:
            result += base*(N % 9)
            N = N // 9
            base = base * 10
        return result

            
obj = Solution()
res = obj.findNth(100)
print(res)

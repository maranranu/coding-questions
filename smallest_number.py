"""
Given an array of size N, find the smallest positive integer value that cannot be represented as sum of some elements from the array.

Input: 
N = 6
array[] = {1, 10, 3, 11, 6, 15}
Output: 
2
Explanation:
2 is the smallest integer value that cannot 
be represented as sum of elements from the array.

"""
class Solution:
    def smallestpositive(self, array, n):
        selem = set()
        array.sort()
    
        result = 1
        
        for i in range(0, n):
            if array[i] <= result:
                result += array[i]
        return result
 
t = int(input())

for i in range(t):
  n = int(input())
  arr = [int(x) for x in input().strip().split(' ')]
  obj = Solution()
  print(obj.smallestpositive(arr, n))

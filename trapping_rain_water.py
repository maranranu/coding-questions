"""
Given an array arr[] of N non-negative integers representing the height of blocks. 
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10
"""
class Solution:
    def trappingWater(self, arr,n):
        left = 0 
        right = n - 1
        
        lmax = 0
        rmax = 0
        lmaxi = -1
        rmaxi = -1
        
        cnt = 0
        
        while left <= right:
            if arr[left] < arr[right]:
                if lmax < arr[left]:
                    lmaxi = left
                    lmax = arr[left]
                else:
                    cnt += (lmax - arr[left])
                left += 1
            else:
                if rmax < arr[right]:
                    rmax = arr[right]
                    rmaxi = right
                else:
                    cnt += (rmax - arr[right])
                
                right -= 1
        return cnt
 
t = int(input())
obj = Solution()

for i in range(t):
  n = int(input())
  arr = [int(x) for x in input().rstrip().split(' ')]
  res = obj.trappingWater(arr, n)
  print(res)

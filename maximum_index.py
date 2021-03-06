"""
Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].
"""
def maxIndexDiff(arr, n): 
    maxrray = [0] * n
    minrray = [0] * n
    
    minrray[0] = arr[0]
    for i in range(1, n):
        minrray[i] = min(arr[i], minrray[i-1])
    
    maxrray[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        maxrray[i] = max(arr[i], maxrray[i + 1])
    
    maxdiff = 0
    i = 0
    j = 0
    
    while i < n and j < n:
        if minrray[i] <= maxrray[j]:
            maxdiff = max(maxdiff, j - i)
            j = j + 1
        else:
            i = i + 1
    
    return maxdiff

t = int(input())

for i in range(t):
  n = int(input())
  arr = [int(x) for x in input().rstrip().split(' ')]
  res = maxIndexDiff(arr, n)
  print(res)

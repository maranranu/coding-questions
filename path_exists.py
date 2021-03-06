"""
Given a grid of size n*n filled with 0, 1, 2, 3. Check whether there is a path possible from the source to destination. You can traverse up, down, right and left.
The description of cells is as follows:

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Wall.
Note: There are only a single source and a single destination.
Input: grid = {{3,0,3,0,0},{3,0,0,0,3}
,{3,3,3,3,3},{0,2,3,0,0},{3,0,0,1,3}}
Output: 0
Explanation: The grid is-
3 0 3 0 0 
3 0 0 0 3 
3 3 3 3 3 
0 2 3 0 0 
3 0 0 1 3 
There is no path to reach at (3,1) i,e at 
destination from (4,3) i,e source.
"""
class Solution:
    def isSafe(self, u, v, row, col):
        return u >= 0 and u < row and v >= 0 and v < col
        
	def is_Possible(self, grid):
		q = []
		row = len(grid)
		col = len(grid[0])
		
		for i in range(row):
		    for j in range(col):
		        if grid[i][j] == 1:
		            q.append([i,j])
		            break
		neig = [(-1, 0), (1, 0), (0, 1), (0, -1)]

		while len(q):
		    temp = q.pop(0)
		    u = temp[0]
		    v = temp[1]
		    
		    if not self.isSafe(u, v, row, col):
		        continue
		    
		    if grid[u][v] == 0:
		        continue
		    
		    if grid[u][v] == 2:
		        return True
		        
		    grid[u][v] = 0
		    
		    for n in neig:
		        i = u + n[0]
		        j = v + n[1]
		        
		        q.append([i, j])
		
		return False

obj = Solution()

t = int(input())
for i in range(t):
  n = int(input())
  grid = []
  for i in range(n):
    arr = [int(x) for x in input().strip().split(' ')]
    grid.append(arr)
  ans = obj.is_Possible(grid)
  print(ans)

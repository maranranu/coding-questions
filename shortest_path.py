#code

class Solution:
    def isSafe(self, row, col, u, v, path, visit):
        return u >= 0 and u < row and v >= 0 and v < col and path[u][v] == 1 and not visit[u][v]
        
    def shortest_path(self, path, row, col, destination):
        q = []
        if path[0][0] == 0:
            return -1
        q.append([0, 0])
        
        time = 0
        visit = [[False for c in range(col)] for r in range(row)]
        
        while len(q) > 0:
            i, j = q.pop(0)
            
            visit[i][j] = True
            
            if destination[0] == i and destination[1] == j:
                return time
            
            if path[i][j] == 0:
                continue
            
            if self.isSafe(row, col, i - 1, j, path, visit):
                q.append([i - 1, j])
            
            if self.isSafe(row, col, i + 1, j, path, visit):
                q.append([i + 1, j])
            
            if self.isSafe(row, col, i, j - 1, path, visit):
                q.append([i, j - 1])
            
            if self.isSafe(row, col, i, j + 1, path, visit):
                q.append([i, j + 1])
            
            time += 1
        return -1

t = int(input())

for i in range(t):
    rc = input()
    row, col = [int(r) for r in rc.split(' ')]
    ele = input()
    elements = [int(r) for r in ele.split(' ')]
    rd, cd = [int(r) for r in input().split(' ')]
    
    cnt = 0
    matrix = [[0 for c in range(col)] for r in range(row)]
    
    for i in range(row):
        for j in range(col):
            matrix[i][j] = elements[cnt]
            cnt += 1
    obj = Solution()
    res = obj.shortest_path(matrix, row, col, [rd, cd])
    print(res)

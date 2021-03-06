"""
Aterp is the head nurse at city hospital. City hospital contains R*C number of wards and structure of hospital is in the form of a 2-D matrix.
Given a matrix of dimension R*C where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty ward
1 : Cells have uninfected patients
2 : Cells have infected patients

An infected patient at ward [i,j] can infect other uninfected patient at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. Help Aterp determine the minimum units of time after which there won't remain any uninfected patient i.e all patients would be infected. If all patients are not infected after infinite units of time then simply return -1.

"""
from collections import deque

class Solution:
    def isSafe(self, u, v, row, col):
        return u >= 0 and u < row and v >= 0 and v < col
    
    def endReached(self, elem):
        return elem[0] == -1 and elem[1] == -1
    
    def checkall(self, row, col, arr):
        for i in range(row):
            for j in range(col):
                if (arr[i][j] == 1):
                    return False
        return True
        
    def helpaterp(self, hospital):
        # code here
        q = deque()
        row = len(hospital)
        col = len(hospital[0])
        time = 0
        
        for i in range(row):
            for j in range(col):
                if hospital[i][j] == 2:
                    q.append([i, j])
        q.append([-1, -1])
        
        while True:
            check = False
            while not self.endReached(q[0]):
                temp = q[0]
                if self.isSafe(temp[0]+1, temp[1], row, col) and hospital[temp[0]+1][temp[1]] == 1:
                    hospital[temp[0]+1][temp[1]] = 2
                    if not check:
                        time += 1
                        check = True
                    q.append([temp[0]+1, temp[1]])
                
                if self.isSafe(temp[0] - 1, temp[1], row, col) and hospital[temp[0] - 1][temp[1]] == 1:
                    hospital[temp[0] - 1][temp[1]] = 2
                    if not check:
                        time += 1
                        check = True
                    q.append([temp[0] - 1, temp[1]])
                
                if self.isSafe(temp[0], temp[1] - 1, row, col) and hospital[temp[0]][temp[1] - 1] == 1:
                    hospital[temp[0]][temp[1] - 1] = 2
                    if not check:
                        time += 1
                        check = True
                    q.append([temp[0], temp[1] - 1])
                
                if self.isSafe(temp[0], temp[1] + 1, row, col) and hospital[temp[0]][temp[1] + 1] == 1:
                    hospital[temp[0]][temp[1] + 1] = 2
                    if not check:
                        time += 1
                        check = True
                    q.append([temp[0], temp[1] + 1])

                q.popleft()
            
            q.popleft()
            q.append([-1, -1])
            if len(q) == 1 and self.endReached(q[0]):
                break
        
        if not self.checkall(row, col, hospital):
            return -1
        else:
            return time

obj = Solution()
hospital = [[2,1,0,2,1], [1,0,1,2,1], [1,0,0,2,1]]
ans = obj.helpaterp(hospital)
print(ans)

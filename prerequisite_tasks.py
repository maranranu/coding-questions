"""
There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, for example to do task 0 you have to first complete task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.
Input: 
N = 4, P = 3
prerequisites = {{1,0},{2,1},{3,2}}
Output:
Yes
Explanation:
To do task 1 you should have completed
task 0, and to do task 2 you should 
have finished task 1, and to do task 3 you 
should have finished task 2. So it is possible.
"""
from collections import defaultdict 

class Graph:
    def __init__(self, nodes):
        self.graph = defaultdict(list)
        self.nodes = nodes
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCycle(self, v, visit, stack):
        visit[v] = True
        stack[v] = True
        
        for neighbour in self.graph[v]:
            if not visit[neighbour]:
                if self.isCycle(neighbour, visit, stack):
                    return True
            elif stack[neighbour]:
                return True
        stack[v] = False
        return False
        
class Solution:         
    def isPossible(self, numCourses, prerequisites):
        graph = Graph(numCourses)
        visit = [False] * numCourses
        stack = [False] * numCourses
        
        for p in prerequisites:
            graph.addEdge(p[0], p[1])
            
        for course in range(numCourses):
            if not visit[course]:
                if graph.isCycle(course, visit, stack):
                    return False
        return True
  
t = int(input())
for i in range(t):
  n = int(input())
  p = int(input())
  prerequisite = []
  for i in range(p):
    pair = [int(x) for x in input().split(' ')]
    prerequisite.append(pair)
  
  obj = Solution()
  if obj.isPossible(n, prerequisite):
    print("YES")
  else:
    print("NO")

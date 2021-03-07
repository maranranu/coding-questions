from collections import deque

class Graph:
    def __init__(self, n):
        self.graph = {}
        self.node = n
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def bfs(self, u, destination, visit):
        queue = deque()
        
        queue.append((u, 0))
        visit.add(u)
        
        while len(queue) > 0:
            v, count = queue.popleft()
            
            if v == destination:
                return count + 1
            
            for c in range(len(v)):
                st = v[0:c] + '*' + v[c+1:]

                if st in self.graph:
                    for edge in self.graph[st]:
                        if edge not in visit:
                            queue.append((edge, count + 1))
        return 0
        
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        n = len(set(wordList))
        g = Graph(n)
        
        if targetWord not in wordList:
            return 0
        
        if startWord not in wordList:
            wordList.append(startWord)
        
        for i in range(0, len(wordList)):
            word = wordList[i]
            
            for c in range(len(word)):
                key = word[0:c] + '*' + word[c+1:]
                g.addEdge(key, word)

        visit = set()
        return g.bfs(startWord, targetWord, visit)

t = int(input())

for i in range(t):
    n = int(input())
    wordList = []
    for i in range(n):
        wordList.append(input().strip())
    startWord = input()
    targetWord = input()
    obj = Solution()
    ans = obj.wordLadderLength(startWord,targetWord,wordList)
    print(ans)

"""
startWord = "der"
targetWord = "dfs"
words = ["des", "der", "dfr", "dgt", "dfr", "dfs"]
#outpout: 3

startWord = "gedk"
targetWord = "geek"
words = ["geek", "gefk"]
#output: 0

startWord = "TOON"
targetWord = "PLEA"
words = ["POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"]
#output: 7

startWord = "ABCV"
targetWord = "EBAD"
words = ["ABCD", "EBAD", "EBCD", "XYZA"]
#output: 4
"""

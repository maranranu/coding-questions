"""
Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths. Find the length of the shortest transformation sequence from startWord to targetWord.
Keep the following conditions in mind:

A word can only consist of lowercase characters.
Only one letter can be changed in each transformation.
Each transformed word must exist in the dictionary.
The second part of this problem can be found here.


Example 1:

Input:
wordList = {"des","der","dfr","dgt","dfr","dfs"}
startWord = "der", targetWord= "dfs",
Output:
3
Explanation:
The length of the smallest transformation
sequence from "der" to "dfs" is 3
i,e "der" -> "dfr" -> "dfs".
"""
from collections import deque

class Solution:
    def bfs(self, start, target, wordList):
        queue = deque()
        visit = set()
        queue.append((start, 0))
        visit.add(start)
        
        while len(queue) > 0:
            v, count = queue.popleft()
            
            if v == target:
                return count + 1
            
            for i in range(len(v)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    st = v[0:i] + c + v[i+1:]
                    
                    if st in wordList and st not in visit:
                        queue.append((st, count + 1))
                        visit.add(st)
        return 0

    def wordLadderLength(self, startWord, targetWord, wordList):
        if targetWord not in wordList or startWord == targetWord:
            return 0
        
        return self.bfs(startWord, targetWord, set(wordList))

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

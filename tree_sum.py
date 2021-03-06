# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    def levelordersum(self, root):
        queue = [root]
        maxsum = root.val
        minsum = root.val

        while len(queue):
            count = len(queue)
            s = 0

            while count > 0:
                node = queue.pop(0)
                s += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                count -= 1
            maxsum = max(maxsum, s)
            minsum = min(minsum, s)
        return (maxsum, minsum)

root = Node(4)
root.left      = Node(2)
root.right     = Node(-5)
root.left.left  = Node(-1)
root.left.right = Node(3)
root.right.left = Node(-2)
root.right.right = Node(6)

obj = Solution()
print("levelorder sum: ", obj.levelordersum(root))

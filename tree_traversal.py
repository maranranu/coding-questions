# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def inorder(self, root, rslt):
        if root:
            self.inorder(root.left, rslt)
            rslt.append(root.val)
            self.inorder(root.right, rslt)
        return rslt

    def preorder(self, root, rslt):
        if root:
            rslt.append(root.val)
            self.preorder(root.left, rslt)
            self.preorder(root.right, rslt)
        return rslt

    def postorder(self, root, rslt):
        if root:
            self.postorder(root.left, rslt)
            self.postorder(root.right, rslt)
            rslt.append(root.val)
        return rslt
    
    def levelorder(self, root, rslt):
        queue = [root]

        while len(queue):
            node = queue.pop(0)
            rslt.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return rslt

    def bottomLeftMost(self, root):
        queue = [root]
        
        while len(queue):
            node = queue.pop(0)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
    
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)

obj = Solution()
print("Inorder: ", obj.inorder(root, []))
print("Preorder: ", obj.preorder(root, []))
print("Postorder: ", obj.postorder(root, []))
print("levelorder: ", obj.levelorder(root, []))
print(obj.bottomLeftMost(root))

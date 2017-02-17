class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

class Solution:

    def invert(self,root):
        self.inv(root)
    
    def inv(self,node):
        left = node.left
        right = node.right
        node.right = left
        node.left = right
        if left is not None:
            self.inv(left)
        if right is not None:
            self.inv(right)
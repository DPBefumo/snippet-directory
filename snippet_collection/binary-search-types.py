"""
Notes:
"""

"""
Problem:
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, root, pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        # If there is no root, then we are looking at an empty tree, and should return -1
        if not root:
            return -1
        # If we are at the edge of a tree, on a leaf node, there would be no left and no right, and the height would be 0
        if not root.left and not root.right:
            return 0
        # Get the left and right height on the nodes children by calling the getHeight function recursively
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        # Return the 1 plus the max of left or right
        return max(left_height, right_height) + 1
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
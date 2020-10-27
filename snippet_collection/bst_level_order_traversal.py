"""
Notes:
"""

"""
Problem:
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, root, pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.
"""

import sys

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

    def levelOrder(self,root):
        # Use list as a working queue, since you can append to the end and pop from the beginning to use it like a queue
        nodes_to_traverse = list()
        # Make a string to keep track of the nodes we have traversed so we can print at the end
        nodes_traversed = ''
        # Start of the queue with the root node. Seed the queue with all the roots at the start
        nodes_to_traverse.append(root)
        # While the queue is not empty, we will pop off the front node to traverse it, if it has children, they will be added to the queue and then the front node will be added to the string of nodes_traversed 
        while len(nodes_to_traverse) > 0:
            node = nodes_to_traverse.pop(0)
            if node.left:
                nodes_to_traverse.append(node.left)
            if node.right:
                nodes_to_traverse.append(node.right)
            # Add to string of nodes traversed
            nodes_traversed += str(node.data) + ' '
        # Exit while loop and print the nodes traversed
        print(nodes_traversed)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
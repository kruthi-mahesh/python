"""Print height of binary search tree
sample input:
7
3
5
2
1
4
6
7
Sample ouptut :
3
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
    def getHeight(self, root):
        if root == None:
            return -1
        else:
            return 1 + max( self.getHeight(root.left), self.getHeight(root.right) )
        
t=int(input())
myTree=Solution()
root=None
for i in range(t):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)   
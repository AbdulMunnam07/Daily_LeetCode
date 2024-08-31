# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            subList = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    subList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if subList:
                res.append(subList)

        return res
           
        
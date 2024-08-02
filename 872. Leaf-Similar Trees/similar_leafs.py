class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(root,  leaf):
            if not root:
                return 

            if not root.left and not root.right:
                leaf.append(root.val)

            dfs(root.left, leaf)
            dfs(root.right, leaf)
        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2
        
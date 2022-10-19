class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: list[TreeNode]) -> int:
        '''
        n - number of vertexes
        h - max height of tree

        time  --- O(n)
        space --- O(h)
        '''
        if root is None: return 0
        
        def dfs(root: TreeNode) -> int:
            if root.left is None and root.right is None:
                return 1

            if root.left is None:
                return 1 + dfs(root.right)

            if root.right is None:
                return 1 + dfs(root.left)

            return 1 + max(dfs(root.right), dfs(root.left))

        return dfs(root)


def test():
    a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7, right=TreeNode(8))))
    b = TreeNode(2)

    s = Solution()

    assert s.maxDepth(a) == 4
    assert s.maxDepth(b) == 1


if __name__ == "__main__":
    test()

        
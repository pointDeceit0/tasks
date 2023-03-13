class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # attempt to create Tree from list, but because of the fact that tree is assymetric a lot depends of input
        # For example:
        # [9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6] 
        # The answer is 16
        # But tree can be interpretated different, then answer will be 15
        if isinstance(val, int):
            self.val   = val
            self.left  = left
            self.right = right

        elif isinstance(val, list):   
            temp = val.copy()
            def _create_tree(val: int, i: int) -> TreeNode:
                # от левых и правых то тоже нужно создавать
                r = TreeNode(val, 
                             TreeNode(_create_tree(temp[i * 2 + 1], i * 2 + 1)) if i * 2 + 1 < len(temp) and temp[i * 2 + 1] else None, 
                             TreeNode(_create_tree(temp[i * 2 + 2], i * 2 + 2)) if i * 2 + 2 < len(temp) and temp[i * 2 + 2] else None)
                return r
            self = _create_tree(val[0], 0)
        

class Solution:
    '''
        Didn't find any other ideas of solutions

        time  --- O(n) 
        space --- O(1)
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        
        max_path = root.val
        def _dfs(leaf: TreeNode) -> int:
            nonlocal max_path
            if not leaf: 
                return 

            l = _dfs(leaf.left) 
            r = _dfs(leaf.right) 

            max_path = max(leaf.val + l + l, max_path)
            
            return max(leaf.val + max(l, r), 0)
        
        _dfs(root)
        return max_path
    

def test():
    s = Solution()

    a = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.maxPathSum(a) == 6
    print("Done")

    a = TreeNode(1, TreeNode(-2), TreeNode(3))
    assert s.maxPathSum(a) == 4
    print("Done")


def main():
    test()


if __name__ == "__main__":
    main()
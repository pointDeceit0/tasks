# graph clone
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        old_new = {}
        def _clone(n: 'Node') -> 'Node':
            if n in old_new:
                return old_new[n]
            
            new_node = Node(n.val)
            old_new[n] = new_node
            for nei in n.neighbors:
                new_node.neighbors.append(_clone(nei))
            return new_node
        
        return _clone(node)

def test():
    a = Solution()



if __name__ == "__main__":
    test()
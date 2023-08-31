class List(list):
    pass


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Mine ~ 10 times slower than the one below

        nodes = {}

        def check(node: int, leaves: List[int], already_checked: List[int]):
            
            for v in leaves:
                if v in already_checked:
                    continue
                if node == v:
                    return False    
                if v in nodes:
                    already_checked.add(v)
                    if not check(node, nodes[v], already_checked):
                        return False
                    
            return True

            for leaf, node in prerequisites:
                if node not in nodes:
                    nodes[node] = {leaf}
                else:
                    nodes[node].add(leaf)
                if not check(node, nodes[node], set()):
                    return False
            
            return True
        '''
        # Most efficient
        nodes = {}

        def check(node: int, already_checked: List[int]):
            if nodes.get(node) == True: return True
            
            if nodes.get(node):
                for v in nodes[node]:
                    if nodes.get(v) == True: continue
                    if v in already_checked: return False
                    if v in nodes:
                        already_checked.add(v)
                        if not check(v, already_checked):
                            return False
                        
                nodes[node] = True
            return True

        for leaf, node in prerequisites:
            if node not in nodes:
                nodes[node] = {leaf}
            else:
                nodes[node].add(leaf)
        
        return all(check(n, set()) for n in nodes.keys())


def test():
    a = Solution()

    assert a.canFinish(2, [[1,0],[0,1]]) == False
    assert a.canFinish(5, [[1, 2], [3, 4], [3, 1], [5, 1], [4, 5], [4, 1], [5, 2]]) == True
    assert a.canFinish(4, [[1, 2], [2, 3], [3, 4], [4, 1]]) == False
    assert a.canFinish(4, [[1, 2], [2, 3], [3, 1]]) == False
    assert a.canFinish(0, []) == True

    assert a.canFinish(5, [[1, 2], [3, 4], [5, 3], [3, 1], [5, 1], [4, 5], [4, 1], [5, 2]]) == False

    assert a.canFinish(2, [[1,0]])       == True
    assert a.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])       ==  False



if __name__ == "__main__":
    test()
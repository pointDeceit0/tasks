class List(list):
    pass


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        it will cache right in the graph

        time  O(n)
        space O(n), actually O(n) + O(n)
        '''
        graph = {}
        for v, p in prerequisites:
            if v not in graph:
                graph[v] = {p}
            else:
                graph[v].add(p)
            
        def dfs(v: int, were: set) -> bool:
            # check if in cache -> true
            if graph.get(v) == True:
                return True

            # if vertex in graph(like key) -> going by each its linked vertexes
            if graph.get(v, 0):
                for prereq in graph[v]:
                    if graph.get(prereq) == True:
                        continue
                    
                    if prereq in were:
                        return False
                    # condition to get rid of unnecessary recursion AND if in cache
                    if graph.get(prereq, False):# and not cache.get(v, False):
                        were.add(prereq)
                        if not dfs(prereq, were):
                            return False
                        
                graph[v] = True
                return True

            else:
                return True
        
        return all(dfs(i, set()) for i in graph.keys())


def test():
    a = Solution()

    assert a.canFinish(5, [[1, 2], [3, 4], [3, 1], [5, 1], [4, 5], [4, 1], [5, 2]]) == True
    assert a.canFinish(2, [[1,0],[0,1]]) == False
    assert a.canFinish(4, [[1, 2], [2, 3], [3, 4], [4, 1]]) == False
    assert a.canFinish(4, [[1, 2], [2, 3], [3, 1]]) == False
    assert a.canFinish(0, []) == True

    assert a.canFinish(5, [[1, 2], [3, 4], [5, 3], [3, 1], [5, 1], [4, 5], [4, 1], [5, 2]]) == False

    assert a.canFinish(2, [[1,0]])       == True
    assert a.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])       ==  False



if __name__ == "__main__":
    test()
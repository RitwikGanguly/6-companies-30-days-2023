class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        edge = [[] for i in range(n)]
        degree = [0] * n

        for a, b in prerequisites:
            edge[b].append(a)
            degree[a] += 1

        l = [i for i in range(n) if degree[i] == 0] #dfs

        for i in l:
            for j in edge[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    l.append(j)

        return len(l) == n
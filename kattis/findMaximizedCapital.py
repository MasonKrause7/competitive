from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = sorted(zip(capital, profits))
        i = 0
        heap = []
        n = len(projects)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1

            if not heap:
                return w

            w -= heappop(heap)
        return w

s = Solution()
k=11
w=11
profits = [1,2,3]
capital = [11,12,13]
print(s.findMaximizedCapital(k, w, profits, capital))

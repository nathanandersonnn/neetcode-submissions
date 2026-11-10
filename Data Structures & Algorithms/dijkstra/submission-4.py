class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        visited = {}
        pqueue = []
        heapq.heappush(pqueue, (0, src))
        while pqueue:
            val, temp = heapq.heappop(pqueue)
            if temp in visited: continue
            visited[temp] = val
            for src, neighbor, tempval in edges:
                if src != temp: continue
                rand = tempval + val
                heapq.heappush(pqueue, (rand, neighbor))
        for i in range(n):
            if i not in visited: visited[i] = -1
        return visited
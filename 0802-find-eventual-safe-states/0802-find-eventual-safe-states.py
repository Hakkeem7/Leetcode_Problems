class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # 0 = unvisited
        # 1 = visiting
        # 2 = safe
        state = [0] * n

        def dfs(node):

            # If currently visiting, cycle found
            if state[node] == 1:
                return False

            # Already confirmed safe
            if state[node] == 2:
                return True

            # Mark as currently visiting
            state[node] = 1

            # Check all possible paths
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # No cycle found from this node
            state[node] = 2

            return True

        answer = []

        for node in range(n):
            if dfs(node):
                answer.append(node)

        return answer
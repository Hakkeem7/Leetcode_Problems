class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict

        # Step 1: Build adjacency list
        graph = defaultdict(list)

        for source, target, time in times:
            graph[source].append((target, time))

        # Step 2: Min-heap
        # (current_time, node)
        heap = [(0, k)]

        # Stores shortest time to each node
        distance = {}

        # Step 3: Dijkstra's Algorithm
        while heap:
            current_time, node = heapq.heappop(heap)

            # Already processed with shortest distance
            if node in distance:
                continue

            distance[node] = current_time

            # Explore neighbors
            for neighbor, travel_time in graph[node]:

                if neighbor not in distance:
                    new_time = current_time + travel_time

                    heapq.heappush(
                        heap,
                        (new_time, neighbor)
                    )

        # If not all nodes received the signal
        if len(distance) != n:
            return -1

        # The last node to receive the signal
        return max(distance.values())
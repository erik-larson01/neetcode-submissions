class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord("A")] += 1
        maxHeap = [-count for count in counts if count > 0]
        heapq.heapify(maxHeap)
        
        time = 0

        # Tracks tasks that are unable to be run
        queue = deque() # [remainingCount, nextAvailableTime]

        while maxHeap or queue:
            time += 1
            if maxHeap:
                # Run task
                remainingCount = heapq.heappop(maxHeap)
                remainingCount += 1
                if remainingCount < 0:
                    queue.append([remainingCount, time + n])
            if queue and queue[0][1] <= time:
                # Add back to heap to be ran
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
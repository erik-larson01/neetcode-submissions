class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord("A")] += 1
        
        maxHeap = [-count for count in counts if count > 0]
        heapq.heapify(maxHeap)

        # Counter to track time elapsed
        time = 0
        # Store pairs of [remainingCount, next_available_time]
        queue = deque() # Stores tasks you cannot run yet

        while maxHeap or queue:
            time += 1
            if maxHeap:
                # Remove (run) task with largest remainingCount
                remainingCount =  1 + heapq.heappop(maxHeap)
                # Add it to the cooldown queue
                if remainingCount < 0:
                    queue.append([remainingCount, time + n])
            # Check cooldown queue
            if queue and queue[0][1] <= time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time

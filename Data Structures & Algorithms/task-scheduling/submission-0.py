class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Strategy: Get hashmap of all elements and then frequencies
        # Find the task with the most frequency, and then run one of them first
        # Then, while there are other unique tasks and num tasks ran after is less than n, run the other unique tasks
        # Do this as much as possible until there are no more unique tasks left
        # Use heap to keep track of CPU cycles in between a

        freq = Counter(tasks)
        maxHeap = [freq[key] for key in freq]
        heapq.heapify_max(maxHeap)

        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush_max(maxHeap, queue.popleft()[0])

        return time
        
        

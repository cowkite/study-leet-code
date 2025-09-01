import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (t - p) / (t * (t + 1))

        heap: List[Tuple[float, int, int]] = []
        for p, t in classes:
            heap.append((-gain(p, t), p, t))
        heapq.heapify(heap)

        for _ in range(extraStudents):
            neg_g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(heap)

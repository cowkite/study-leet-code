import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # 한 명(무조건 합격)을 더 넣었을 때 그 반의 통과비율이 얼마나 증가하는지
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - (p / t)

        # 초기 힙 만들기: 가장 이득(gain)이 더 큰 반을 빠르게 꺼내기 위해
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # broilliant 학생들을 하나씩 배정
        for _ in range(extraStudents):
            neg_g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # 최종 평균
        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(heap)

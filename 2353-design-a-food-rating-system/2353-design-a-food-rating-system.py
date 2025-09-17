from typing import List, Dict, Tuple
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # 각 음식의 현재 상태: food -> (cuisine, rating)
        self.food_info: Dict[str, Tuple[str, int]] = {}
        # 요리종류별 최대 힙: cuisine -> [(-rating, name)]
        self.by_cuisine: Dict[str, List[Tuple[int, str]]] = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = (c, r)
            if c not in self.by_cuisine:
                self.by_cuisine[c] = []
            heapq.heappush(self.by_cuisine[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, _old = self.food_info[food]
        # 상태 갱신
        self.food_info[food] = (c, newRating)
        # 새 상태를 힙에 추가 (이전 상태는 게으른 삭제로 처리)
        heapq.heappush(self.by_cuisine[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.by_cuisine[cuisine]
        # 힙 꼭대기가 현재 상태와 다르면 버린다 (게으른 삭제)
        while heap:
            neg_r, name = heap[0]
            cur_c, cur_r = self.food_info[name]
            # 동일 요리종류이며 점수가 일치하면 최신 상태
            if cur_c == cuisine and -neg_r == cur_r:
                return name
            # 아니면 오래된 엔트리이므로 버림
            heapq.heappop(heap)
        # 문제 조건상 최소 1개는 있으므로 여기 도달하지 않음
        return ""

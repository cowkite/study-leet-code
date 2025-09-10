from collections import Counter

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        know = [set()] + [set(langs) for langs in languages]

        cannot = [] # 대화 불가 (u, v) 목록
        U = set()   # 가르칠 필요가 생길 수 있는 후보 사용자 집합

        for u, v in friendships:
            if know[u].isdisjoint(know[v]):
                cannot.append((u, v))
                U.add(u)
                U.add(v)

        # 이미 모두 소통 가능하면
        if not cannot:
            return 0
        
        lang_freq = Counter()
        for u in U:
            for l in know[u]:
                lang_freq[l] += 1

        
        need_min = float('inf')
        U_size = len(U)

        for l in range(1, n + 1):
            # 이 언어 l을 이미 아는 후보 사용자 수
            already = lang_freq.get(l, 0)
            need = U_size - already
            if need < need_min:
                need_min = need

        return need_min


                

            

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # 0 = num1 - [ (2^i1 + 2^i2 + ... + 2^ik) + k*num2 ]
        # 2^i1 + 2^i2 + ... + 2^ik = num1 - k*num2
        # num1 - k*num2를 K개의 2거듭제곱 합으로 표현이 가능한지. 가능하다면 K 반환, 불가능하다면 0 반환

        def popcount_greedy(S: int) -> int:
            cnt = 0
            while S > 0:
                # S보다 작거나 같은 가장 큰 2의 거듭제곱 찾기
                p = 1
                while p * 2 <= S:
                    p *= 2
                S -= p
                cnt += 1
            return cnt

        for k in range(1, 61):
            S = num1 - k * num2
            if S < 0:
                if num2 > 0:
                    # num2가 양수면 이후 k는 더 불리해지므로 바로 종료
                    break
                else:
                    # num2가 음수/0이면 다음 k에서 S가 커질 수 있으니 계속 진행
                    continue

            minPieces = popcount_greedy(S)

            # k개의 2의 거듭제곱 합으로 S를 만들 수 있는지
            if minPieces <= k <= S:
                return k

        return -1


        
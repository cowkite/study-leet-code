class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # 마지막 행을 시작 dp로 사용
        dp = triangle[-1][:]  # 복사 (원본 보존)

        # 아래에서 위로
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])

        return dp[0]
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # 모음 개수가 0개면 무조건 False
        # 모음 개수가 홀수면 무조건 True

        # 모음 개수가 짝수일 때 True
        # 마지막 홀수번째 모음 뒤에가 자음이면 True / 모음이면 

        vowelsCount = 0
        VOWELS = set("aeiou")
        for ch in s:
            if ch in VOWELS:
                vowelsCount += 1

        return True if not vowelsCount == 0 else False
        
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            r = n - i
            if "0" not in str(i) and "0" not in str(r):
                return [i, r]

        return []
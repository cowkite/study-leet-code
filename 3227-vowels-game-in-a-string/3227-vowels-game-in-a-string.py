class Solution:
    def doesAliceWin(self, s: str) -> bool:
        VOWELS = set("aeiou")
        for ch in s:
            if ch in VOWELS:
                return True
        return False
        
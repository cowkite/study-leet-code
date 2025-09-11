class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = set("aeiouAEIOU")

        vowels = sorted([ch for ch in s if ch in VOWELS])

        vi = 0
        ans = []

        for ch in s:
            if ch in VOWELS:
                ans.append(vowels[vi])
                vi += 1
            else:
                ans.append(ch)

        return "".join(ans)

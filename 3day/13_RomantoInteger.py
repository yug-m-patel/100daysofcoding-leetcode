class Solution:
    def romanToInt(self, s: str) -> int:
        reff = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 }
        intiger = 0
        n = len(s)

        for i in range(n):
            if i < (n - 1) and reff[s[i]] < reff[s[i + 1]]:
                intiger -= reff[s[i]]
            else:
                intiger += reff[s[i]]
        return intiger

class Solution:
    def titleToNumber(self, s: str) -> int:
        count = 0
        k=len(s)
        for i in s:
            # print(i)
            count = count + (ord(i) - 64) * (26 ** (k - 1))
            k -= 1
        return count
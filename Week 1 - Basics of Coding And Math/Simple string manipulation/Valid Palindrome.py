class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum())
        s = (s.lower())
        print(s)
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
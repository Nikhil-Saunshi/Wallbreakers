class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        print(s)
        l, r = 0, len(s)-1
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while l < r:
            if s[l] not in vowel:
                l += 1
            if s[r] not in vowel:
                r -= 1  
            if s[l] in vowel and s[r] in vowel:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
        print(s)
        return "".join(s)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = hashcheck(s)
        h1 = hashcheck(t)
        
        if h1 == h:
            return True
        else: return False
        
        
def hashcheck( s):
    h = {}
    for i in s:
        if i in h:
            h[i] = h[i] +1
        else:
            h[i] = 1
    return h

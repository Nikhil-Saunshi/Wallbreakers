class UF(object):
    def __init__(self, n):
        self.u = list(range(n))
        
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.u[ra] = rb
    
    def find(self, a):
        while self.u[a] != a: a = self.u[a]
        return a

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        l = len(M)
        
        uf = UF(l)
        for r in range(l):
            for c in range(r,l):
                if M[r][c] == 1: 
                    uf.union(r,c)
                    
        return len(set([uf.find(i) for i in range(l)]))
        
        
#         count = 0
#         for r in range(len(M)):
#             for c in range(len(M[0])):
#                 print(r, c, M[r][c])
#                 if M[r][c] == 1:
#                     # M[r][c] = 0
#                     count += 1
#                     print(count, M)
#                     self.dfs(r, c, M)
#                     print(M)

#         return count
                
        
        
#     def dfs(self, lo, hi, M ):
#         if lo <= hi:
#             return 0
        
#         elif M[lo][hi] == 0:
#             return
        
#         elif M[lo][hi] == 1:
#             M[lo][hi] = 0
#             return self.dfs(lo, hi + 1, M)
#             return self.dfs(lo, hi - 1, M)
#             return self.dfs(lo + 1, hi, M)
#             return self.dfs(lo - 1, hi, M)
        
        
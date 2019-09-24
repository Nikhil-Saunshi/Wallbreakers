class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        l = len(A)
        for i in range( l):
            A[i] = A[i][::-1]
        print(A)
        
        for i in range(l):
            # A[i].reverse()
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A
class Solution:
    def binaryGap(self, N: int) -> int:
        arr = list(bin(N))[2:]
        print(arr)
        l = r = m = 0
        while(r < len(arr)):
            if arr[r] == '1':
                m = max(m , r-l)
                l = r
                r+= 1
            else:
                # l += 1
                r += 1
        return m
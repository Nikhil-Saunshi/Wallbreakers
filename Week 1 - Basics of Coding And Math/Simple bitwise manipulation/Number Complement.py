class Solution:
    def findComplement(self, num: int) -> int:
        # print(num,  num.bit_length(), 2**num.bit_length()-1)
        # Exor operation inverts the number 
        return num ^ (2**num.bit_length()-1)
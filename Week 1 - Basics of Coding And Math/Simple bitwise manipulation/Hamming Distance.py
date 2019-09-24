class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in bin(x^y)[2:]: #Binary returns in a form of 1b00.... So slicing the number to a binary number by removing the first 2 characters
            if i == '1': #Binary returns string, so compare with '1' instread of 1.
                count += 1
        return count
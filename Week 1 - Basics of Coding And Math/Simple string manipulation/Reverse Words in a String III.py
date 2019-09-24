class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        temp = s.split()
        for i in temp:
            e = i[::-1]
            res.append(e)
            # print(e, res)
            # res += [" "]
        return ' '.join(res)
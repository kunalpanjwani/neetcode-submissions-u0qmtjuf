class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        dct = {"[":"]","(":")","{":"}"}
        open = []
        close = []
        for i in s:
            if i in (dct.keys()):
                open.append(i)
                continue
            if open and i == dct[open[-1]]:
                open.pop()
            else:
                return False
        if not open:
            return True
        return False
                
        

        # print(l,l/2)
        # if l%2 != 0:
        #     return False
        # dct = {"[":"]","(":")","{":"}"}
        # for i in range(l//2):
        #     print(s[i],s[-1-i])
        #     if dct[s[i]]==s[-1-i]:
        #         continue
        #     else:
        #         return False
        # return True
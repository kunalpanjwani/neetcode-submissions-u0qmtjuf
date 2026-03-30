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
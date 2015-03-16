class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        alen = len(a)
        blen = len(b)
        if alen > blen:
            b = "".join(["0"]*(alen-blen)) + b
        elif blen > alen:
            a = "".join(["0"]*(blen-alen)) + a
        maxlen = max(alen, blen)
        
        ans = ""
        c = 0
        for i in range(maxlen).__reversed__():
            try:
                ai = int(a[i])
            except IndexError:
                ai = 0
            try:
                bi = int(b[i])
            except IndexError:
                bi = 0
            resi = ai + bi + c
            if resi == 3:
                ans += "1"
                c = 1
            elif resi == 2:
                ans += "0"
                c = 1
            elif resi == 1:
                ans += "1"
                c = 0
            else:
                ans += "0"
        if c:
            ans += str(c)
        return ans[::-1]

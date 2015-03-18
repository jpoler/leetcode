## looks like I may have oversolved this problem.
## see round2.py in the same dir to see one that runs 3x faster

import operator
class Solution:
    substr_len = 10
    base = 256
    # total cop-out, I don't have time to write miller-rabin right now
    # and why isn't there a batteries included python library for prime
    # finders anyway???
    mod = 2**64 - 59
    

    def __init__(self):
        self.rh = 0
        self.hashes = {}
        self.s = None
    

    
    def insert_new_hash(self, hash, str_start, str_end):
        try:
            strings = self.hashes[hash]
        except:
            strings = {}
            self.hashes[hash] = strings
        strings[self.s[str_start:str_end]] = str_start

    
    def findRepeatedDnaSequences(self, s):
        if len(s) < self.substr_len:
            return []
        self.s = s
        start = 0
        stop = 0
        shift_out = self.base**(self.substr_len-1)
        for i in range(self.substr_len):
            self.rh = (self.rh*self.base + ord(s[i])) % self.mod
        # self.insert_new_hash(self.rh, 0, 10)
        for i in range(len(self.s)-(self.substr_len-1)):
            if self.rh in self.hashes:
                self.insert_new_hash(self.rh, i, i+self.substr_len)
            else:
                self.hashes[self.rh] = {}

            if i < len(self.s) - self.substr_len:
                high_char = ord(self.s[i])*shift_out
                if self.rh >= high_char:
                    self.rh = (self.base*(self.rh - high_char) + ord(self.s[i+self.substr_len])) % self.mod
                else:
                    self.rh = (self.base*self.rh + (self.mod - (self.base*high_char % self.mod)) + ord(self.s[i+self.substr_len])) % self.mod
            
        ans = []
        for h, dct in self.hashes.items():
            for string, index in dct.items():
                ans.append((index, string))
        ans = sorted(ans, key=operator.itemgetter(0))
        return [string for index, string in ans]
            
   
if __name__ == '__main__':
    string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = Solution()
    print(s.findRepeatedDnaSequences(string))
        
        

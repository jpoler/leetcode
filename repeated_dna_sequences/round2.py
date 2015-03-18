class Solution:
    
    def findRepeatedDnaSequences(self, s):
        substrings = {}
        answers = []
        done = {}
        n = len(s)
        m = 10
        for i in range(n-m+1):
            sub = s[i:i+m]
            if sub in substrings:
                if sub not in done:
                    answers.append(sub)
                done[sub] = True
            else:
                substrings[sub] = True
        return answers

if __name__ == '__main__':
    string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = Solution()
    print(s.findRepeatedDnaSequences(string))

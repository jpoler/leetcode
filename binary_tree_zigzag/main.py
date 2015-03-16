class Solution:
    def zigzagLevelOrder(self, root):
        self.levels = {}
        self.max_depth = 0
        self.recur(root, 0)
        r = False
        ans = []
        if self.levels:
            for i in range(self.max_depth+1):
                if r == True:
                    ans.append(self.levels[i][::-1])
                else:
                    ans.append(self.levels[i])
                r = not r
        return ans

        


    def recur(self, n, depth):
        if not n:
            return
        if depth > self.max_depth:
            self.max_depth = depth
        try:
            l = self.levels[depth]
        except KeyError:
            l = []
            self.levels[depth] = l
        l.append(n.val)
        self.recur(n.left, depth + 1)
        self.recur(n.right, depth + 1)
        

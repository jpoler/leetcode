class Solution:
    def permuteUnique(self, seq):
        done = {}
        def recur(seq):
            if not seq:
                return [[]]
            current_perms = []
            first, rest = seq[0], seq[1:]
            res = recur(rest)
            for perm in res:
                for i in range(len(perm)+1):
                    new_perm = perm[:i] + [first] + perm[i:]
                    if not tuple(new_perm) in done:
                        current_perms.append(new_perm)
                        done[tuple(new_perm)] = True
            return current_perms
        return recur(seq)


if __name__ == '__main__':
    print(unique_perms([1,2,2,1]))

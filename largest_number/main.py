class CmpList(list):
    def __lt__(self, other):
        for i in range(min(len(self), len(other))):
            if self[i] != other[i]:
                return self[i] < other[i]
        if len(self) < len(other):
            return True
        return False

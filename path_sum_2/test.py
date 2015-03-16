import main

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

nodes = [1, [[2, [[], []]], [3, [[], []]]]]
        
def build_tree(nodes):
    
    val = nodes[0]
    n = Node(val)
    left, right = nodes[1]
    if left:
        n.left = build_tree(left)
    if right:
        n.right = build_tree(right)
    return n

t = build_tree(nodes)
s = main.Solution()
print(s.pathSum(t, 4))


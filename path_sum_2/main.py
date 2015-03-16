class Solution:
    def recur(self, node, path, sofar):
        print(node.left, node.right)
        print(node.val)
        return_paths = []
        if node.left == None and node.right == None:
            return [path + [node.val]]
        if sofar > self.max:
            return [[]]
        path = path[:] + [node.val]
        sofar += node.val
        leftres = [[]]
        rightres = [[]]
        if node.left:
            leftres = self.recur(node.left, path, sofar)
        if node.right:
            rightres = self.recur(node.right, path, sofar)
        return_paths.extend(leftres)
        return_paths.extend(rightres)
        return return_paths
    
    def pathSum(self, root, desired_sum):
        print_tree(root)
        self.max = desired_sum
        paths = self.recur(root, [], 0)
        print(paths)
        return [path for path in paths if sum(path) == desired_sum and path]
            
def print_tree(t):
    if t:
        print(t.val)
        print_tree(t.left)
        print_tree(t.right)

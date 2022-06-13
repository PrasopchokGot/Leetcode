class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
    
def depth_first_value(root):
    if root.val == None: 
        return []

    result = []
    stack = [root]

    while (len(stack) > 0):
        current = stack.pop()
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)

        result.append(current.val)
    return result

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(depth_first_value(a))
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

def depth_first_value_recursive(root):
    if root == None: 
        return []

    left_value = depth_first_value_recursive(root.left)
    right_value = depth_first_value_recursive(root.right)

    return [root.val, *left_value, *right_value]

a, b, c, d, e, f = (Node('a'), Node('b'), Node('c'), 
                    Node('d'), Node('e'), Node('f'))

a.left, a.right = (b, c)
b.left, b.right = (d, e)
c.right = f

print(depth_first_value(a) == depth_first_value_recursive(a))
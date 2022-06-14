class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

a, b, c, d, e, f = (Node('a'), Node('b'), Node('c'), 
                    Node('d'), Node('e'), Node('f'))

a.left, a.right = (b, c)
b.left, b.right = (d, e)
c.right = f

def breadth_first_value(root):
    if root == None:
        return []
    result = []
    queue = [root]

    while len(queue) > 0:
        current = queue[0]
        queue.remove(current)
        result.append(current.val)
        
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return result

print(breadth_first_value(a))
"""
        a
        /\
       b  c    Left to Right: [a b c d e f]
      /\   \   Right to Left: [a c b f e d]
     d  e   f
"""
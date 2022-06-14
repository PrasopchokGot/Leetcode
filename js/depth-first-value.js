import {Node} from './Node.js'

const depthFirstValues = root => {
    if (root == null) return []

    const result = []
    const stack = [root]
    while (stack.length > 0) {
        const current = stack.pop();
        result.push(current.val);

        // Order: Left to Right(stack left is on top of right)
        if (current.right) {stack.push(current.right)}
        if (current.left) {stack.push(current.left)}
    }
    return result
};

const depthFirstValues_recursive = root => {
    if (root == null) return []

    const leftValue = depthFirstValues_recursive(root.left);
    const rightValue = depthFirstValues_recursive(root.right);
    
    // Order: Right to Left
    return [root.val, ...rightValue, ...leftValue]
}

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

/*
        a
        /\
       b  c        Left to Right: [a, b, d, e, c, f]
      /\   \       Right to Left: [a, c, f, b, e, d]
     d  e   f
*/
a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

console.log(depthFirstValues_recursive(a))

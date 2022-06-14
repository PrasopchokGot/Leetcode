import {Node} from './Node.js'

const breadthFirstValues = (root) => {
    if (root == null) { 
        return [] 
    }
    
    const result = []
    const queue = [root]

    while (queue.length > 0) {
        const current = queue.shift()
        result.push(current.val)

        if (current.left) {queue.push(current.left)}
        if (current.right) {queue.push(current.right)}
    }
    return result
}

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

[a.left, a.right] = [b, c];
[b.left, b.right] = [d, e];
c.right = f;


console.log(breadthFirstValues(a))

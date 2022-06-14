import {Node} from './Node.js'

const treeIncludes = (root, target) => {
    const queue = [root];
    while (queue.length > 0) {
        const current = queue.shift();
        if (current.val == target) return true;

        if (current.left) queue.push(current.left)
        if (current.right) queue.push(current.right)
    }
    return false;
};

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

[a.left, a.right] = [b, c];
[b.left, b.right] = [d, e];
c.right = f;

console.log(treeIncludes(a, 'j'));

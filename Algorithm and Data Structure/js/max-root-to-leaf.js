import {Node} from './Node.js'

const maxPath = (root) => {
    if (root == null) return 0;
    const maxValue = Math.max(maxPath(root.left), maxPath(root.right))
    return maxValue + root.val
}

const a = new Node(5);
const b = new Node(11);
const c = new Node(3);
const d = new Node(4);
const e = new Node(2);
const f = new Node(1);
// sum of tree = 23

[a.left, a.right] = [b, c];
[b.left, b.right] = [d, e];
c.right = f;

bo
console.log(maxPath(a))
console.log(Boolean(a.left) + Boolean(a.right))
import {Node} from './Node.js'

const treeSumBFS = (root) => {
    if (root == null) return 0;
    let result = 0;
    const stack = [root];

    while (stack.length > 0){
        const current = stack.pop()
        result += current.val

        if (current.left) stack.push(current.left)
        if (current.right) stack.push(current.right)
    }
    return result;
};

const treeSumDFS = (root) => {
    if (root == null) return 0;
    return root.val + treeSumDFS(root.left) + treeSumDFS(root.right)
}

const a = new Node(1);
const b = new Node(2);
const c = new Node(3);
const d = new Node(4);
const e = new Node(5);
const f = new Node(12);
// sum of tree = 23

[a.left, a.right] = [b, c];
[b.left, b.right] = [d, e];
c.right = f;

console.log(treeSumBFS(a))
console.log(treeSumDFS(a))

import {Node} from './Node.js'

const treeMinValue = root => {
    if (root == null) return Infinity;
    return Math.min(treeMinValue(root.left), root.val, treeMinValue(root.right));
}

const treeMinValueBFT = root => {
    let minValue = Infinity;
    const queue = [root];

    while (queue.length > 0) {       
        const curr = queue.shift();
        minValue = Math.min(minValue, curr.val);

        if (curr.left) queue.push(curr.left);
        if (curr.right) queue.push(curr.right); 
    }
    return minValue
};

const treeMinValueDFS = root => {
    let minValue = Infinity;
    const stack = [root];

    while (stack.length > 0) {       
        const curr = stack.pop();
        minValue = Math.min(minValue, curr.val);
        
        if (curr.right) stack.push(curr.right); 
        if (curr.left) stack.push(curr.left);
    }
    return minValue
};

//     a   
//   b   c
//  d e f g

const a = new Node(5);
const b = new Node(11);
const c = new Node(3);
const d = new Node(4);
const e = new Node(15);
const f = new Node(12);

[a.left, a.right] = [b, c];
[b.left, b.right] = [d, e];
c.right = f;

console.log(treeMinValue(a) == treeMinValueBFT(a) 
            && treeMinValueBFT(a) ==treeMinValueDFS(a))
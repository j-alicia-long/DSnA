# Data Structures
Mostly written in Python


## Vectors/Arraylists

### Arrays
- Need to check whether you are using a normal or dynamic array, which has O(1) amortized insertion
  - Dynamic array doubles in size when filled (thus amortized O(1) resize)

#### Common Tricks
- Use double pointers instead of a nested loop (ex. contiguous subarray) for linear runtime
- For 2D arrays, break down into smaller subsets
- Hashtables/hashsets are good for finding duplicates
  - Maximizes runtime with space tradeoff
- Memorize string methods for your language of choice


## Linked Lists
- Always ask if you have the following that makes the problem easier:
  - Tail pointer
  - Doubly-linked?
  - Size method?
  - Edge case: empty/null list

#### Common Tricks
- Many can be solved with a slow/fast pointer (ex. finding a cycle)
- Drawing makes problems easier


## Trees, Tries, Graphs

### Preorder, Inorder, Postorder, Level order
Different ways of traversing the tree
- DFS does pre/in/post order, while BFS does level-order
- You can rebuild any binary tree using inorder and either pre/post order traversal
  - If given just pre and post, you can only construct full binary trees

### Trie - prefix tree
- TrieNodes have a dict of children with char keys (26) that map to more TrieNodes


## Stacks & Queues

### Stacks
- LIFO
- Alway used with DFS
- Keywords: Syntax checking, Recursion, Backtracking, Reversing a word

### Queues
- FIFO
- Always used with BFS
- Keywords: Minimum

#### Priority Queues
- Queue sorted by something specific
  - Ex. numeric value (path length), alphabetically
  - Used in Dijkstra's Algorithm for min path



## Heaps


## Hash Tables

## Explanation to Problems

#### Problem 1 - LRU Cache
For the  LRU_Cache problem, after thinking of using different approaches (included previous failures), it has been decided to use the  OrderedDict(), specifically the use of the method.popitem(last=False). It allows to remove the first added element, which is basic for the priority construction demanded. 

Since the get and set operations are constant time, our Big O Notation is O(1).
Space complexity consists of a node list and a cache dictionary, so our Big O there is O(2n).

Big O Notation
Time: O(1)
Space: O(n)


#### Problem 2 - File Recursion
Since we have to look through every directory to check each file, the best bet is probably recursion. For my function, I simply print the path if the suffix is a match, otherwise I check if it's a directory. If it is a directory, for each file in the directory, we recursively call the function again.

The time complexity is Big O of N times the number of directories, since for each directory we call our function again. The space complexity can grow exponentially with each recursive call.

Big O Notation
Time: O(n)
Space: O(n)


#### Problem 3 - Huffman Encoding/Decoding
let n is the length of string
m length of unique characters k length of huffman tree nodes

Encoding:

Count frequencies: O(n)
Building a priority queue: O(m * log(m)) (priority put is log(n))
Build Huffman Tree: O(k * log(k))
Traverse Huffman Tree: O(k)
Overall: O(n) + O(m * log(m)) + O(k * log(k)) + O(k) = O(k * log(k))
O(n) since it's the least complexity is ignored
O(m log(m)) is ignored, since m is less than k (m is number of leaf nodes, k is number of all nodes)
therefore the overall complexity is O(k * log(k))

Decoding:

n is the length of string
k is the number of k nodes Overall: O(n * log(k))

Iterating over the input data in O(n) and in each iteration we traverse the tree by log(k)

Space Complexity for encoding and decoding:

O(k)

#### Problem 4 - Users in Group
This problem is a bit unclear. I wasn't sure if it was asking us to find a user if nested within a group. But I solved for that since that could use recursion. If the user is in the group we return True. Else, for every group in the group we call our function again and search through users.

Big O Notation Time & Space: O(n)
No matter the size of users and groups, we have to search through them all recursively to find our user. We use two arrays to store our users and groups, so our Big O grows as simple multiples of these for space.


#### Problem 5 - BlockChain
Our Blockchain problem is really just a node and a linked list. Each node in the list points to the next, while also storing the hash of itself, and its previous hash.

Since we merely iterate through a linked list, and do some hashing functions, the Big O for time should be a simple O(1). And Big O for space is 1 for our hash sha and 1 for our linked list: O(2n).
Big O Notation
Time: O(n)
Space: O(n)
Adding a block: O(1)
Printing a block chain: O(n)

#### Problem 6 - Union and Intersection
The `union` function has two while loops, one for each linked list. Therefor its performance is Big O of N times 2: O(2n) or O(n).

The `intersection` function has a loop within a loop, checking for identical values in either list. It's performance is thus a bit worse at Big O of N squared: O(n**2).

In both functions I use Python's `set` function to create a unique cache list of either the union or intersection of the items in both lists. This adds another loop for iterating thru the final set, but it's effect on performance is minimal. With a linked list and a cache set, we have a space Big O of O(2n).

Big O Notation
Time: O(n**2)
Space: O(n)

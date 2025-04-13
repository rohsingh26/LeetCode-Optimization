import ast

tagDict= {
    "Easy": 0, "Medium": 1, "Hard": 2, "Array": 3, "String": 4,
    "Hash Table": 5, "Dynamic Programming": 6, "Math": 7, "Sorting": 8,
    "Greedy": 9, "Depth-First Search": 10, "Binary Search": 11,
    "Database": 12, "Matrix": 13, "Breadth-First Search": 14,
    "Tree": 15, "Bit Manipulation": 16, "Two Pointers": 17,
    "Prefix Sum": 18, "Heap (Priority Queue)": 19, "Simulation": 20, "Binary Tree": 21,
    "Stack": 22, "Graph": 23, "Counting": 24, "Sliding Window": 25,
    "Design": 26, "Enumeration": 27, "Backtracking": 28, "Union Find": 29,
    "Linked List": 30, "Ordered Set": 31, "Number Theory": 32,
    "Monotonic Stack": 33, "Segment Tree": 34, "Trie": 35,
    "Combinatorics": 36, "Bitmask": 37, "Queue": 38, "Recursion": 39,
    "Divide and Conquer": 40, "Memoization": 41, "Binary Indexed Tree": 42,
    "Geometry": 43, "Binary Search Tree": 44, "Hash Function": 45,
    "String Matching": 46, "Topological Sort": 47, "Shortest Path": 48,
    "Rolling Hash": 49, "Game Theory": 50, "Interactive": 51,
    "Data Stream": 52, "Monotonic Queue": 53, "Brainteaser": 54,
    "Doubly-Linked List": 55, "Randomized": 56, "Merge Sort": 57,
    "Counting Sort": 58, "Iterator": 59, "Concurrency": 60,
    "Probability and Statistics": 61, "Quickselect": 62,
    "Suffix Array": 63, "Bucket Sort": 64, "Line Sweep": 65,
    "Minimum Spanning Tree": 66, "Shell": 67, "Reservoir Sampling": 68,
    "Strongly Connected Component": 69, "Eulerian Circuit": 70,
    "Radix Sort": 71, "Rejection Sampling": 72, "Biconnected Component": 73
  }

question=[]
for i in range(586):
    a=input()
    question.append(a[1:])

print("+++")

datatype=[]
for i in range(586):
    a=input()
    b=ast.literal_eval(a)
    datatype.append(b)

print("++++")

level=[]
for i in range(586):
    a=input()
    level.append(a)

tag=[]
for i in range(586):
    x=[]
    x.append(tagDict[level[i]])
    for j in datatype[i]:
        if j in tagDict:
            x.append(tagDict[j])
    tag.append(x)

final=[]
for i in range(586):
    a={}
    a['name']=question[i]
    a['tags']=tag[i]
    final.append(a)

for i in final:
    print(i,',')
# 2D-Binary-Indexed-Tree
Project presented by:
19B-079-CS / Kanwal Iqbal
19B-080-CS / Ali Arham 
Instructor:
Miss Asma Idrees Mala
Dr. Mohammad Qasim Pasta
2D BINARY INDEXED TREE
INTRODUCTION:
First of all to understand the 2d binary indexed tree we  need to understand binary indexed tree Binary Indexed Tree or Fenwick Tree Let us consider the following problem to understand Binary Indexed Tree. We have an array array[0 . . . n-1]. We would like to A simple solution is to run a loop from 0 to i-1 and calculate the sum of the elements. To update a value, simply do array[i] = x. The first operation takes O(n) time and the second operation takes O(1) time. Another simple solution is to create an extra array and store the sum of the first i-th elements at the i-th index in this new array. The sum of a given range can now be calculated in O(1) time, but the update operation takes O(n) time now. This works well if there are a large number of query operations but a very few numbers of update operations.
Use of binary indexed tree:
Binary Indexed Tree also called Fenwick Tree provides a way to represent an array of numbers in an array, allowing prefix sums to be calculated efficiently. For example, an array [2, 3, -1, 0, 6] is given, then the prefix sum of first 3 elements [2, 3, -1] is 2 + 3 + -1 = 4.Using binary Indexed tree also, we can perform both the tasks in O(logN) time. But then why to learn another data structure when segment tree can do the work for us. It’s because binary indexed trees require less space and are very easy to implement.
Two-Dimensional Binary Indexed Tree or Fenwick Tree
We know that to answer range sum queries on a 1-D array efficiently, binary indexed tree (or Fenwick Tree) is the best choice (even better than segment tree due to less memory requirements and a little faster than segment tree).
Can we answer sub-matrix sum queries efficiently using Binary Indexed Tree?
The answer is yes. This is possible using a 2D BIT which is nothing but an array of 1D BIT.
Update:
As we known Binary tree also gives us the option of update in least possible time which is of O(logn).so the question is here how are this going to work in binary tree.
 Fenwick Tree at the start is considered to be built upon a zero matrix, so zero is stored at every position. Update is used with every element of array[][] to build up the Fenwick tree. In 2D binary tree, the algorithm for update is just 2-dimensional version of update used in 1D Fenwick tree. Given (x, y) as co-ordinate to be updated.
Build tree:
Build tree is used to construct a 2D binary indexed tree



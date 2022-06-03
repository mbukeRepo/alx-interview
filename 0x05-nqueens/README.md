## 0x05. N Queens

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**. Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively. **Example 1:** ![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

<pre>Input: n = 4
Output: [[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
</pre>

**Example 2:**

<pre>Input: n = 6
Output: [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
</pre>

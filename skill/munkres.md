---
name: munkres
category: utility
description: munkres algorithm for the Assignment Problem
tags: [munkres, hungarian-algorithm, optimization, assignment-problem, python]
author: oxo-call-community
source_url: "http://software.clapper.org/munkres/"
---

## Concepts

- **Tool Overview**: munkres is a Python implementation of the Munkres algorithm (also known as the Hungarian algorithm or Kuhn-Munkres algorithm). It solves the assignment problem: finding the minimum cost way to assign n workers to n jobs.
- **Core Function**: Takes a cost matrix (n x n) where each element represents the cost of assigning a worker to a job, and computes the optimal assignment that minimizes total cost.
- **Algorithm**: Implements the Hungarian algorithm with O(n³) time complexity. Far more efficient than brute-force enumeration which is O(n!).
- **Input Format**: Accepts a Python list-of-lists or numpy array representing the cost matrix. Can be rectangular (n x m) matrices, which get automatically padded to square.
- **Output**: Returns a list of (row, column) tuples indicating which elements to assign. The sum of assigned elements is the minimum possible total cost.
- **Installation**: Available via pip (`pip install munkres`) and conda (`conda install -c conda-forge munkres`). Pure Python, no external dependencies.

## Pitfalls

- **Cost vs Profit**: The algorithm minimizes cost. To maximize profit/benefit, convert your profit matrix to a cost matrix by subtracting from a large value (e.g., `sys.maxsize - profit`).
- **Rectangular Matrices**: While the algorithm assumes square matrices, munkres automatically pads rectangular matrices with zeros. Be aware that this may affect the optimal assignment.
- **Irregular Matrices**: Only rectangular or square matrices work. Lists with uneven row lengths will cause errors.
- **Large Matrices**: O(n³) complexity means 1000x1000 matrices are slow. Consider scipy.optimize.linear_sum_assignment for large sparse matrices.
- **No Assignment Cost**: The algorithm finds optimal assignment but doesn't return the cost directly. Compute manually with `sum(matrix[r][c] for r, c in result)`.
- **Float vs Int**: Works with both integer and float cost matrices. Float precision issues rarely occur but be aware for very large matrices.

## Examples

### Basic usage
**Args:** `from munkres import Munkres; m = Munkres(); matrix = [[5, 9, 1], [10, 3, 2], [8, 7, 4]]; indexes = m.compute(matrix)`
**Explanation:** Creates a Munkres object and computes the optimal assignment for a 3x3 cost matrix. Returns list of (row, column) pairs.

### Print optimal assignment with costs
**Args:** `m.compute(matrix); print_matrix(matrix, msg='Lowest cost assignment:')`
**Explanation:** After computing, use print_matrix() utility to display the matrix with optimal assignments highlighted.

### Solve rectangular matrix
**Args:** `matrix = [[1, 2, 3], [3, 2, 1]]; m = Munkres(); m.compute(matrix)`
**Explanation:** Handles rectangular matrices automatically. The matrix is conceptually padded with zeros to become square. Useful when you have more workers than jobs or vice versa.

### Maximize instead of minimize
**Args:** `cost_matrix = [[sys.maxsize - v for v in row] for row in profit_matrix]; m.compute(cost_matrix)`
**Explanation:** To maximize total profit, convert profit to cost by subtracting each value from a large constant. Then minimize as usual.

### Real-world: Optimal task assignment
**Args:** `cost = [[10, 15, 20], [12, 8, 14], [18, 11, 12]]; m = Munkres(); assign = m.compute(cost)`
**Explanation:** Example of assigning three workers to three tasks with different costs. The result tells which worker should do which task for minimum total cost.

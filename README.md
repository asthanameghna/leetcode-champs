# LeetCode Solutions

This repository contains my solutions to **LeetCode problems** as part of my preparation for **software engineering and machine learning interviews**.

The objective is to build strong fundamentals in:

- Data Structures
- Algorithms
- Problem Solving
- Time and Space Complexity Analysis

All solutions are implemented in **Python**.

---

# Repository Structure

Problems are grouped by **algorithmic pattern** rather than random order. This mirrors how most interview preparation is structured.

```
leetcode-solutions
│
├── arrays_hashing
├── two_pointers
├── sliding_window
├── stack
├── binary_search
├── linked_list
├── trees
├── heap_priority_queue
├── graphs
├── dynamic_programming
├── greedy
└── backtracking
```


Each solution contains:

- Link to the problem
- Key idea / intuition
- Time complexity
- Space complexity
- Clean implementation

---

# Progress Tracker

| Difficulty | Solved |
|------------|--------|
| Easy       |   16   |
| Medium     |   11   |
| Hard       |   1    |

Total Problems Solved: **0**

---

# Problem List

| Problem | Difficulty | Topic | Solution |
|--------|------------|-------|----------|
| Two Sum | Easy | Arrays / Hashing | [Code](./arrays_hashing/two_sum.py) |
| Valid Parentheses | Easy | Stack | [Code](./stack/valid_parentheses.py) |
| Daily Temperatures | Medium | Stack | [Code](./stack/daily_temperatures.py) |
| Mimimum Window Substring | Hard | Sliding Window | [Code](https://github.com/asthanameghna/leetcode-champs/blob/main/sliding_window/minimum_window_substring.py) |
| 3Sum | Medium | Two Pointers | [Code](https://github.com/asthanameghna/leetcode-champs/blob/main/two_pointers/three_sum.py) |


---

# Study Approach

My preparation strategy focuses on mastering **core algorithmic patterns**, since most interview problems fall into a limited set of categories.

Key patterns include:

- Two Pointers
- Sliding Window
- Monotonic Stack
- Binary Search
- DFS / BFS
- Dynamic Programming
- Greedy
- Backtracking

---

# Example Solution Template

```python
# Problem: Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/

# Approach
# Use a monotonic decreasing stack storing indices.
# When a warmer temperature appears, resolve previous indices.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result
```

## Goals

- 🎯 Solve **300+ problems**
- 🧠 Master **core algorithmic patterns**
- ⏱ Reach **consistent medium-level problem solving under 30 minutes**

---

## LeetCode Profile 
🔗[HERE](https://leetcode.com/u/3EH6PSW9H2/)

# Day 2 – Python Problem Solving & Core Data Structures

Python Developer Placement Preparation Series

## Overview

Day 2 focuses on Python problem-solving techniques, core data structures, coding interview approaches, debugging, and time and space complexity.

## Topics Covered

- Problem-solving workflow and edge cases
- Python list operations: `append()`, `extend()`, `pop()`, `sort()` and `sorted()`
- Dictionaries and sets
- Frequency counting and duplicate detection
- Two-pointer technique
- Palindrome checking
- Sliding window technique
- Time and space complexity
- Debugging using `for/else`

## Assignment Tasks

### Task A: Remove Duplicates While Preserving Order

Objective: Remove duplicate elements from a list while preserving the order of their first occurrence.

Example:

- Input: `[3, 1, 3, 2, 1]`
- Output: `[3, 1, 2]`

Approach: Use a set to track seen elements and a list to store unique elements in their original order.

Complexity:

- Time: O(n) expected
- Space: O(n)

File: `01_remove_duplicates.py`

### Task B: Maximum Sum of a Contiguous Window

Objective: Find the maximum sum of any contiguous window of size `k`.

Example:

- Input: `[2, 1, 5, 1, 3, 2]`, `k = 3`
- Output: `9`

Approach: Calculate the first window sum, then slide the window by subtracting the outgoing element and adding the incoming element.

Invalid window sizes return `None`.

Complexity:

- Time: O(n)
- Auxiliary space: O(1), excluding the initial slice used to calculate the first window

File: `02_sliding_window.py`

### Task C: Debugging Challenge

Objective:Correct a loop that prints `Not found` for every nonmatching element.

Approach: Use `break` when the target is found and `for/else` to print `Not found` only if the loop completes without finding the target.

File: `03_debugging_challenge.py`

### Task D: Data Structures Comparison

| Feature         | List                     | Set                       | Dictionary                        |
| --------------- | ------------------------ | ------------------------- | --------------------------------- |
| Order           | Preserves sequence order | No guaranteed input order | Preserves insertion order of keys |
| Duplicates      | Allowed                  | Unique elements only      | Keys are unique                   |
| Membership      | O(n) average             | O(1) average              | O(1) average for keys             |
| Main use        | Ordered collections      | Uniqueness and membership | Key-value storage                 |
| Backend example | API response items       | Processed user IDs        | User ID to user details           |

File: `04_data_structures.py`

## Test Cases

- Empty list
- Single-element list
- All elements duplicated
- Mixed duplicate and unique elements
- Window size of 1
- Window size equal to the list length
- Invalid window sizes: zero, negative, and greater than the list length
- Lists containing negative numbers

## Project Structure

text
Python-Placement-Preparation/
├── Day-2-Python-Problem-Solving/
│ ├── 01_remove_duplicates.py
│ ├── 02_sliding_window.py
│ ├── 03_debugging_challenge.py
│ ├── 04_data_structures.py
│ └── README.md
└── Day-3-HTTP-FastAPI/

## How to Run

Run each Python file individually from the VS Code terminal:

bash
python 01_remove_duplicates.py
python 02_sliding_window.py
python 03_debugging_challenge.py
python 04_data_structures.py

## Key Learnings

- Using sets for efficient duplicate detection.
- Preserving order while removing duplicates.
- Applying the sliding window technique to reduce repeated calculations.
- Handling edge cases and invalid inputs.
- Debugging loops using `for/else`.
- Comparing lists, sets, and dictionaries.
- Explaining time and space complexity.

## Reflection

What I learned:How to solve common Python coding problems using suitable data structures and efficient techniques.

What I found difficult:Understanding how the sliding window updates its sum without recalculating every element.

What I would improve: Practise more coding problems, test boundary cases, and explain my approach before writing code.

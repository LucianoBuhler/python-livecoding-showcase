# 01 Remove Duplicates

## Description
Remove duplicates from a list while preserving order.

## Instructions
Implement the function in `solution.py`. Add test cases if necessary.

## How to Run
```bash
python solution.py
```


# 01 Remove Duplicates from List (Preserving Order)

## Problem
Given a list of elements, remove duplicates while preserving the original order.

## Input
['a', 'b', 'a', 'c', 'b']

## Output
['a', 'b', 'c']

## Approach
- Use `dict.fromkeys()` which preserves order in Python 3.7+.
- Alternative: use a set to track seen elements.

## Live Coding Tips
- Explain the choice of `dict.fromkeys`.
- Show an alternative with loop + set.
- Write basic tests.

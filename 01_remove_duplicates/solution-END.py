"""
Final solution: Remove duplicates from a list while preserving order.

Approach 1: Using dict.fromkeys (Python 3.7+ preserves order)
Approach 2: Using a set to track seen elements manually

Both run in linear time O(n), but dict.fromkeys is slightly faster for small/medium lists.
"""

# Approach 1: Uses dict.fromkeys to remove duplicates while preserving order.
def remove_duplicates_v1(lst):
    return list(dict.fromkeys(lst))

# Approach 2: Manually track seen elements using a set.
def remove_duplicates_v2(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    INITIAL_LIST = ['a', 'b', 'a', 'c', 'b']
    print("#" * 80)
    print("# Challenge 1: Remove duplicates from a list while preserving order.")
    print("#" * 80)
    print("# Input: ")
    print(INITIAL_LIST)
    print("# Output v1: using dict.fromkeys")
    print(remove_duplicates_v1(INITIAL_LIST))  # ['a', 'b', 'c']
    print("Output v2: using manual set")
    print(remove_duplicates_v2(INITIAL_LIST))  # ['a', 'b', 'c']
    print("#" * 80) 

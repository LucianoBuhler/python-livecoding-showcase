# 03 Reverse Words

## Description
Reverse the order of words in a sentence.

## Example Input
sentence = "the sky is blue"

## Expected Output
"blue is sky the"

## Instructions
Implement the function in `solution-START.py`. Add test cases if necessary.

## How to Run
```bash
python solution-END.py
```

## Solutions

### ✅ Solution 1 – Split and reverse
- Split the sentence into a list of words
- Reverse the list and join it back into a string

### ✅ Solution 2 – Manual character traversal
- Manually parse the string to build words and reverse their order
- Useful in environments where `.split()` or list comprehension is restricted

## How to Run

```bash
# Default (uses 'the sky is blue')
python 03_reverse_words/solution-END.py

# Custom sentence
python 03_reverse_words/solution-END.py "hello world from CLI"

"""
Solution: Reverse Words in a Sentence

Approach 1: Split and reverse using list
Approach 2: Manual character traversal (no split)
"""

def reverse_words_v1(sentence):
    return ' '.join(sentence.split()[::-1])

def reverse_words_v2(sentence):
    words, word, result = [], '', ''
    for char in sentence:
        if char == ' ':
            if word:
                words.append(word)
                word = ''
        else:
            word += char
    if word:
        words.append(word)
    for w in reversed(words):
        result += w + ' '
    return result.strip()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Reverse words in a sentence")
    parser.add_argument("sentence", type=str, nargs="?", default="the sky is blue",
                        help="Sentence to reverse")
    args = parser.parse_args()

    print("#" * 80)
    print("# Challenge 3: Reverse the words in a sentence")
    print("#" * 80)

    print("# Using reverse words v1")
    print(reverse_words_v1(args.sentence))

    print("# Using reverse words v2")
    print(reverse_words_v2(args.sentence))

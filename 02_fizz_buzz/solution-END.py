"""
Solution: FizzBuzz from 1 to n

Approach 1: Basic if-elif
Approach 2: Concise string concatenation
"""

def fizz_buzz_v1(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) 

def fizz_buzz_v2(n):
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)  # Print the number if output is empty

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run FizzBuzz up to n")
    parser.add_argument("n", type=int, nargs="?", default=15, help="Maximum number to print")
    args = parser.parse_args()

    print("#" * 80)
    print("# Challenge 2: Print numbers from 1 to n with FizzBuzz rules.")
    print("#" * 80)

    print("# Using fizz buzz v1")
    fizz_buzz_v1(args.n)

    print("# Using fizz buzz v2")
    fizz_buzz_v2(args.n)
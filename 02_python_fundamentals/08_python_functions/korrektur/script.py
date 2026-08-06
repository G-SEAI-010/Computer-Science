# 1. Sum of List Elements
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# 2. Repeated Greeting
def repeat_greeting(name, times):
    for _ in range(times):
        print(f"Hallo, {name}.")


# 3. Factorial Calculation
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 4. Fibonacci Sequence Generator
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    seq = [0, 1]

    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])

    # for _ in range(2, n):
    #     seq.append(seq[-1] + seq[-2])

    return seq


# 5. Maximum of Two Numbers
def max_of_two(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None

    # return a if a > b else b if a < b else None


# 6. Print a Pattern with Nested Loops
def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()

    # for i in range(1, rows + 1):
    #     print("*" * i)


# --- Testaufrufe ---

# Test 1. Sum of List Elements
print("Summe der Liste [1,2,3,4]:", sum_list([1, 2, 3, 4]))

# Test 2. Repeated Greeting
print("\nWiederholte Begrüßung:")
repeat_greeting("Alice", 3)

# Test 3. Factorial Calculation
print("\nFakultät von 5:", factorial(5))

# print()
# for num in [0, 1, 2, 3, 4, 5, 10]:
#     print(f"{num}! = {factorial(num)}")

# Test 4. Fibonacci Sequence Generator
print("\nDie ersten 7 Fibonacci-Zahlen:", fibonacci(7))

# Test 5. Maximum of Two Numbers
print("\nMaximum von 10 und 20:", max_of_two(10, 20))

# Test 6. Print a Pattern with Nested Loops
print("\nDreiecksmuster mit 5 Zeilen:")
print_triangle(5)

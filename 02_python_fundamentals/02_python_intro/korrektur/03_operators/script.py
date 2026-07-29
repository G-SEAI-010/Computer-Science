# Step 1: Arithmetic Operators (Arithmetische Operatoren)
a = 15
b = 4

# Perform arithmetic operations
print("Addition:", a + b)
print("Subtraktion:", a - b)
print("Multiplikation:", a * b)
print("Division:", a / b)
print("Abgerundete Division:", a // b)
print("Modulo:", a % b)
print("Exponenten:", a**b)

# Step 2: Assignment Operators (Zuweisungsoperatoren)
x = 10

x += 5
print("\nNach +=:", x)
x -= 3
print("Nach -=:", x)
x *= 2
print("Nach *=:", x)
x /= 4
print("Nach /=:", x)

# Step 3: Comparison Operators (Vergleichsoperatoren)
print("\na == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Step 4: Logical Operators (Logische Operatoren)
is_python_fun = True
is_java_fun = False

print("\nand:", is_python_fun and is_java_fun)
print("or:", is_python_fun or is_java_fun)
print("not:", not is_python_fun)

# Step 5: Identity Operators (Identitätsoperatoren)
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("\nlist1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)
print("list1 is list3:", list1 is list3)

# Step 6: Membership Operators (Zugehörigkeitsoperatoren)
text = "Python macht Spaß!"

print("\n'Python' in text:", "Python" in text)
print("'Java' nicht in text:", "Java" not in text)

# Step 7: Bitwise Operators (Bonus) (Bit Operatoren)
a = 5
b = 3

print("\na & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("a << 1:", a << 1)
print("b >> 1:", b >> 1)

# Step 8: Operator Precedence (Operatorenrangfolge)
print("\nOhne Klammern 2 + 3 * 4 ** 2:", 2 + 3 * 4**2)
print("Mit Klammern (2 + 3) * (4 ** 2):", (2 + 3) * (4**2))
print("Mit Klammern ((2 + 3) * 4) ** 2:", ((2 + 3) * 4) ** 2)

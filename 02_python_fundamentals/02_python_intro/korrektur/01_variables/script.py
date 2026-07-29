# Step 1: Create variables:
name = "Testy McTest"
age = 100
height = 2.00

# Step 2: Print the variables:
print("name:", name)
print("age:", age)
print("height:", height)

# Step 3: Check the type of the variables:
print("\nTyp von name:", type(name))
print("Typ von age:", type(age))
print("Typ von height:", type(height))

# Step 4: Casting
age_str = str(age)
print(f"\nMein Name ist {name} und ich bin {age_str} Jahre alt.")

# Bonus: Global Variable
global_message = "Hallo aus dem globalen Scope."
print("\nVor der Funktion:", global_message)


def update_global_message():
    global global_message
    global_message = "Hallo aus dem Funktions-Scope"
    print("Innerhalb der Funktion:", global_message)


update_global_message()
print("Nach der Funktion:", global_message)

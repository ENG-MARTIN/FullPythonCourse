def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")

#  ======================== RETURNING ====================
def add(x, y):
    """This function adds two numbers and returns the result."""
    return x + y

result = add(3, 5)
print(result)  # Output: 8

# ======================= DEFAULT PARAMETERS ======================
def power(base, exponent=2):
    """This function raises 'base' to the power of 'exponent'."""
    return base ** exponent

print(power(3))      # Output: 9 (default exponent is 2)
print(power(3, 3))   # Output: 27


# ======================  **kwargs and *args  ==========================
# A function can accept a variable number of arguments using *args (for positional arguments) and **kwargs (for keyword arguments).
def multi_add(*args):
    """This function adds all the numbers passed as arguments."""
    result = 0
    for num in args:
        result += num
    return result

print(multi_add(1, 2, 3, 4))   # Output: 10

# ========================= LAMBDA FUNCTIONS ================================
square = lambda x: x**2
print(square(5))   # Output: 25

# ================ SCOPE ========================
global_var = 10

def my_function():
    local_var = 5
    print(global_var)   # Accessing global variable is okay
    print(local_var)    # Accessing local variable

my_function()
print(global_var)   # Output: 10
# print(local_var)  # This would raise an error, local_var is not defined in this scope

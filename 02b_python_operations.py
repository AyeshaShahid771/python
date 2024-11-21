a = 10
b = 3

print("Addition:", a + b)              # 13
print("Subtraction:", a - b)           # 7
print("Multiplication:", a * b)        # 30
print("Division:", a / b)              # 3.3333...
print("Division without the remainder:", a // b)  # 3
print("Floor Division:", a // b)       # 3
print("Modulus:", a % b)               # 1
print("Exponentiation:", a ** b)       # 1000

 # Python follows the PEMDAS/BODMAS rule for order of operations:

# Parentheses
# Exponents
# Multiplication and Division (left to right)
# Addition and Subtraction (left to right)#

result = (5 + 3) * (2 ** 3) / 4 - 1
print("(5 + 3) * (2 ** 3) / 4 - 1 =", result)  # Output: 15.0
# Start with the expression
# result = (5 + 3) * (2 ** 3) / 4 - 1

# Evaluate Parentheses:
# (5 + 3) → 8
# Now the expression is:
# result = 8 * (2 ** 3) / 4 - 1

# Evaluate Exponents:
# (2 ** 3) → 8 (because 2^3 = 8)
# Now the expression is:
# result = 8 * 8 / 4 - 1

# Multiplication and Division (from left to right):
# First, evaluate 8 * 8 → 64
# Now the expression is:
# result = 64 / 4 - 1

# Then, evaluate 64 / 4 → 16.0
# Now the expression is:
# result = 16.0 - 1

# Subtraction:
# Finally, evaluate 16.0 - 1 → 15.0

# Final result
# result = 15.0


# to set  input to selective decimal places
result = 10 / 3
print(f"{result:.2f}")  # Output: 3.33


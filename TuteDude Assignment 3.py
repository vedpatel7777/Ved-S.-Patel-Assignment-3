# Task 1
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = int(input("Enter a non-negative integer to compute its factorial: "))
print(f"Factorial of {number} is: {factorial(number)}")

# Task 2
import math

number = float(input("Enter a number: "))

sqrt_result = math.sqrt(number)
ln_result = math.log(number)
sin_result = math.sin(number)

print(f"Square root of {number}: {sqrt_result}")
print(f"Natural logarithm of {number}: {ln_result}")
print(f"Sine of {number} (in radians): {sin_result}")
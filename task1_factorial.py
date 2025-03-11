# Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Main program
if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        fact = factorial(num)
        print(f"Factorial of {num} is: {fact}")
    except ValueError:
        print("Please enter a valid integer.")
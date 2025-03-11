# Task 2: Using the Math Module for Calculations

import math

def calculate_math_operations(number):
    sqrt_result = math.sqrt(number)
    log_result = math.log(number)
    sine_result = math.sin(number)
    return {
        "Square Root": sqrt_result,
        "Logarithm": log_result,
        "Sine": sine_result
    }

# Main program
if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        if num <= 0:
            print("Please enter a positive number for logarithm calculation.")
        else:
            results = calculate_math_operations(num)
            print(f"Square root: {results['Square Root']}")
            print(f"Logarithm: {results['Logarithm']}")
            print(f"Sine: {results['Sine']}")
    except ValueError:
        print("Please enter a valid number.")
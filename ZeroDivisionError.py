try:
    numerator = int(input())
    denominator = int(input())
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric values.")
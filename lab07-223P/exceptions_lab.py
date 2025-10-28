def divide_numbers(numerator, denominator):
    try:
        number = numerator/denominator
    excpet ZeroDivisionError:
        print("Error: Division by zero")
    else:
        return number

def parse_int(value):
    try:
        number = int(value)
    except ValueError:
        print("Error: Invalid integer")
    else:
        return number

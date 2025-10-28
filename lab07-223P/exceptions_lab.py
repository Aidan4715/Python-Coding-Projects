def divide_numbers(numerator, denominator):
    try:
        number = numerator/denominator
    excpet ZeroDivisionError:
        print("Error: Division by zero")
    else:
        return number
        
class PrimeNotFoundError(Exception):
    pass


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

def custom_exception(value):
    loop = value - 1
    for (i+2) in range(loop):
        if(value%i = 0):
            raise PrimeNotFoundError("Given number is not prime number")
    return value

    
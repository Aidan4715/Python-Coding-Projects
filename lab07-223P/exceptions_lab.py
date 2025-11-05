class PrimeNotFoundError(Exception):
    pass


def divide_numbers(numerator, denominator):
    try:
        number = numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero"
    else:
        return number


def parse_int(value):
    try:
        number = int(value)
    except ValueError:
        return "Error: Invalid integer"
    else:
        return number


def custom_exception(value):
    if value < 2:
        raise PrimeNotFoundError("Given number is not prime number")
    for i in range(2, value):
        if value % i == 0:
            raise PrimeNotFoundError("Given number is not prime number")
    return value


def palindrome_exception(value):
    if isinstance(value, int):
        raise ValueError
    try:
        if value == value[::-1]:
            return value
        else:
            return "cannot find palindrome"
    except:
        return "cannot find palindrome"


def chain_exception(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        raise Exception("Chained Exception: File operation failed") from e


def cleanup(filename):
    file = None
    try:
        file = open(filename, 'w')
        file.write("Test content")
    finally:
        print("Cleanup complete")
        if file:
            file.close()


def type_error(param1, param2):
    try:
        result = param1 + param2
        return result
    except TypeError:
        return "Error: Incompatible types for addition"
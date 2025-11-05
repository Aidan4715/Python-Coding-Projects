import exceptions_lab


print("=" * 60)
print("Testing divide_numbers function:")
print("=" * 60)

result = exceptions_lab.divide_numbers(10, 2)
print(f"divide_numbers(10, 2) = {result}")

result = exceptions_lab.divide_numbers(10, 0)
print(f"divide_numbers(10, 0) = {result}")

result = exceptions_lab.divide_numbers(15, 4)
print(f"divide_numbers(15, 4) = {result}")
print()


print("=" * 60)
print("Testing parse_int function:")
print("=" * 60)

result = exceptions_lab.parse_int("42")
print(f"parse_int('42') = {result}")

result = exceptions_lab.parse_int("hello")
print(f"parse_int('hello') = {result}")

result = exceptions_lab.parse_int("3.14")
print(f"parse_int('3.14') = {result}")
print()


print("=" * 60)
print("Testing custom_exception function:")
print("=" * 60)

try:
    result = exceptions_lab.custom_exception(7)
    print(f"custom_exception(7) = {result}")
except exceptions_lab.PrimeNotFoundError as e:
    print(f"custom_exception(7) raised: {e}")

try:
    result = exceptions_lab.custom_exception(10)
    print(f"custom_exception(10) = {result}")
except exceptions_lab.PrimeNotFoundError as e:
    print(f"custom_exception(10) raised: {e}")

try:
    result = exceptions_lab.custom_exception(2)
    print(f"custom_exception(2) = {result}")
except exceptions_lab.PrimeNotFoundError as e:
    print(f"custom_exception(2) raised: {e}")
print()


print("=" * 60)
print("Testing palindrome_exception function:")
print("=" * 60)

result = exceptions_lab.palindrome_exception("racecar")
print(f"palindrome_exception('racecar') = {result}")

result = exceptions_lab.palindrome_exception("hello")
print(f"palindrome_exception('hello') = {result}")

result = exceptions_lab.palindrome_exception(121)
print(f"palindrome_exception(121) = {result}")
print()


print("=" * 60)
print("Testing chain_exception function:")
print("=" * 60)

try:
    result = exceptions_lab.chain_exception("nonexistent_file.txt")
    print(f"chain_exception('nonexistent_file.txt') = {result}")
except Exception as e:
    print(f"chain_exception('nonexistent_file.txt') raised: {e}")
    print(f"Caused by: {e.__cause__}")
print()


print("=" * 60)
print("Testing cleanup function:")
print("=" * 60)

exceptions_lab.cleanup("test_output.txt")
print("File operation completed")
print()


print("=" * 60)
print("Testing type_error function:")
print("=" * 60)

result = exceptions_lab.type_error(5, 10)
print(f"type_error(5, 10) = {result}")

result = exceptions_lab.type_error("hello", " world")
print(f"type_error('hello', ' world') = {result}")

result = exceptions_lab.type_error(5, "hello")
print(f"type_error(5, 'hello') = {result}")
print()
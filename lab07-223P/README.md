

# Lab: Errors and Exceptions in Python

## Program Instructions
1. Create a module named exceptions_lab.
     1. Function: divide_numbers
          * Parameters: numerator and denominator.
          * Behavior:
               * Attempt to perform the division numerator / denominator.
               * Use a try/except block to catch a ZeroDivisionError.
               * If a ZeroDivisionError occurs, return the message "Error: Division by zero".
               * If no exception occurs, return the result of the division.

     2. Function: parse_int
          * Parameter: value.
          * Behavior:
               * Attempt to convert value to an integer.
               * Use a try/except block to catch a ValueError.
               * If a ValueError occurs, return the message "Error: Invalid integer".
               * If conversion is successful, return the integer value.

     3. User-Defined Exception: PrimeNotFoundError
          * Define a class named PrimeNotFoundError that inherits from Exception.
          
     4. Function: custom_exception
          * Parameter: value
          * Behavior:
               * If value is not a prime number, raise a PrimeNotFoundError with a descriptive message indicating that the given number is not prime are not allowed.
               * Otherwise, return the value.

     5. Function: palindrome_exception
          * Paramter: value
          * Behavior:
               * If value is an integer, raise ValueError
               * If value is a palindrome string (word spell same backward), return value
               * Use try/except block to catch any other exceptions. If an exception is found, return `cannot find palindrome` 
     
     6. Function: chain_exception
          * Parameter: filename
          * Behavior:
               * Attempt to open the file specified by filename in read mode.
               * If the file does not exist, catch the FileNotFoundError and raise a new Exception with the message "Chained Exception: File operation failed", using exception chaining (i.e., with the from keyword).

     7. Function: cleanup
          * Parameter: filename
          * Behavior:
               * Attempt to open the file in write mode.
               * Use a try/finally block to ensure that a cleanup message "Cleanup complete" is printed regardless of whether an exception occurs.
               * If an exception is raised during the file operation, it should be propagated after executing the cleanup.

     8. Function: type_error
          * Parameters: Two positional parameters.
          * Behavior:
               * Attempt to add these two parameters.
               * Use a try/except block to catch a TypeError.
               * If a TypeError occurs, return the message "Error: Incompatible types for addition".
               * If addition is successful, return the result.


2. Create a main driver program to meet the following requirements:
     1. Create a file named main.py.
     2. Import the exceptions_lab module.
     3. Call each function with appropriate test values to demonstrate exception handling:
          * For chain_exception, pass a filename that does not exist to trigger the exception.
          * For cleanup, observe that the cleanup message is printed regardless of any exceptions.
     4. Testing Your Functions:
          * For each function, write sample test cases that display the function’s input and output.
          * Use inline comments to explain the test case and the expected result.
     5. Execution Block:
          * Use the following block to ensure tests run only when the module is executed directly:


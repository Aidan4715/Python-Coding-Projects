# Laboratory 10

## Laboratory Objective:
    - Familiar with Python Standard Library (PSL)

## Program Instructors:
1. Create `get_current_directory()` function that will return the current working directory

2. Create `list_files_name(directory)` that will return a list of all files that contain `directory`

3. Create `get_command_line()` that will return all command line argument

4. Create `get_number(text)` that will return list of all numbers found in `text`

5. Create `calculate_statistic(my_list)` that will:
    1. Calculate the mean, median, and variance of a list 
    2. Store those values into a list, with the key being the `mean`, `median`, `variance`
    3. Ex: `{"mean": 1.2, ...}`

6. Create `get_current_datetime()` that will return a current date time formatted string:
    1. The format string will be: `"HH:MM:SS MM-DD-YYYY"`

7. Create `measure_executing_time(code, number)` that will:
    1. Set the default value for number to be 10000
    2. Take a string code and return the time it takes to execute the code 

8. Create `logging(message, level, filename)` that:
    1. Set the default value for `filename` to `logging.txt`
    2. Take `level` and `messsage`, the function will log the messags with the given type.
Both `level` and `message` are string input

9. Create `custom_template(template_text, custom_delimiter, kwargs)` that:
    1. Set the default value for `delimiter` to `"$"`
    2. Create a custom template class that use the given `delimiter`
    3. The function will take unlimited keyword arguments. Replace the placeholder text with the value associate with each keyword

10. Create `decimal_precision(decimal, precision)`:
    1. Set the default precision to 4
    2. Take unlimited numbers of decimal numbers and multiply them together. Reverse the given precision point

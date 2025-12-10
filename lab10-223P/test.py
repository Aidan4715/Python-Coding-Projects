import unittest
import stdlib

import os

class Test01_STDLIB_GET_CURRENT_DIRECTORY(unittest.TestCase):
    def test_get_current_directory(self):
        """
        *** Test01 *** FUNCTION CALL: stdlib.get_current_directory()  
        
        *** EXPECT: Current working directory path as string ***
        """
        current_dir = stdlib.get_current_directory()
        self.assertEqual(current_dir, os.getcwd())
        print()

class Test02_STDLIB_LIST_PYTHON_FILES(unittest.TestCase):
    def test_list_python_files(self):
        """
        *** Test02 *** FUNCTION CALL: stdlib.list_python_files(directory='.')  
        
        *** EXPECT: List of Python files in the current directory ***
        """
        python_files = stdlib.list_python_files(directory='.')
        expected_files = [file for file in os.listdir('.') if file.endswith('.py')]
        self.assertEqual(sorted(python_files), sorted(expected_files))
        print()

class Test03_STDLIB_GET_COMMAND_LINE_ARGS(unittest.TestCase):
    def test_get_command_line_args(self):
        """
        *** Test03 *** FUNCTION CALL: stdlib.get_command_line_args()  
        
        *** EXPECT: List of command-line arguments ***
        """
        cmd_args = stdlib.get_command_line_args()
        expected_args = os.sys.argv
        self.assertEqual(cmd_args, expected_args)
        print()

class Test04_STDLIB_FIND_NUMBERS(unittest.TestCase):
    def test_find_numbers(self):
        """
        *** Test04 *** FUNCTION CALL: stdlib.find_numbers(text)  
        
        *** EXPECT: List of number sequences found in the text ***
        """
        text = "There are 2 apples and 15 bananas."
        numbers = stdlib.find_numbers(text)
        expected_numbers = ['2', '15']
        self.assertEqual(numbers, expected_numbers)
        print()

class Test05_STDLIB_CALCULATE_STATISTICS(unittest.TestCase):
    def test_calculate_statistics(self):
        """
        *** Test05 *** FUNCTION CALL: stdlib.calculate_statistics(data)  
        
        *** EXPECT: Dictionary with mean, median, and variance of the data list ***
        """
        data = [1, 2, 3, 4, 5]
        stats = stdlib.calculate_statistics(data)
        expected_stats = {
            "mean": 3,
            "median": 3,
            "variance": 2.5
        }
        self.assertEqual(stats, expected_stats)
        print()

class Test06_GET_CURRENT_DATETIME(unittest.TestCase):
    
    def test_get_current_datetime(self):
        """
        *** Test06 *** FUNCTION CALL: stdlib.get_current_datetime()  
        
        *** EXPECT: Current date and time as a datetime object ***
        """
        from datetime import datetime
        now = datetime.now()
        formatted = now.strftime("%H:%M:%S %m-%d-%Y")
        current_dt = stdlib.get_current_datetime()
        self.assertEqual(current_dt, formatted)
        print()

class TEST07_STBLID_MEASURING_EXECUTION_TIME(unittest.TestCase):
    def test_measure_execution_time(self):
        """
        *** Test07 *** FUNCTION CALL: stdlib.measure_execution_time(func, *args, **kwargs)  
        
        *** EXPECT: Execution time of the function in seconds ***
        """
        code = """
            total = 0
            for i in range(x):
                total += i
            return total
        """
        exec_time = stdlib.measure_execution_time("sum(range(100))", 10000)
        self.assertIsInstance(exec_time, float)
        self.assertGreater(exec_time, 0)
        print()

class Test08_STDLIB_LOGGING(unittest.TestCase):
    def test_logging(self):
        """
        *** Test08 *** LOGGING TEST  
        
        *** EXPECT: Log messages written to log.txt file ***
        """
        log_file = "test.txt"
        if os.path.exists(log_file):
            os.remove(log_file)
        
        stdlib.logging("Debug message for testing.", "debug", filename=log_file)
        stdlib.logging("Info message for testing.", "info",filename=log_file)
        stdlib.logging("Warning message for testing.", "warning",filename=log_file)
        stdlib.logging("Error message for testing.", "error",filename=log_file)
        stdlib.logging("Critical message for testing.", "critical",filename=log_file)
        
        self.assertTrue(os.path.exists(log_file))
        
        with open(log_file, 'r') as f:
            log_contents = f.read()
            self.assertIn("DEBUG: Debug message for testing.", log_contents)
            self.assertIn("INFO: Info message for testing.", log_contents)
            self.assertIn("WARNING: Warning message for testing.", log_contents)
            self.assertIn("ERROR: Error message for testing.", log_contents)
            self.assertIn("CRITICAL: Critical message for testing.", log_contents)
        os.remove(log_file)
        print()
        
class Test09_STDLIB_DECIMAL_PRECISION(unittest.TestCase):
    def test_decimal_precision(self):
        """
        *** Test09 *** DECIMAL PRECISION TEST  
        
        *** EXPECT: Decimal arithmetic with specified precision ***
        """
        from decimal import Decimal, getcontext 
        getcontext().prec = 4
        result = Decimal("0.1400") * Decimal("1.0000")
        self.assertEqual(stdlib.decimal_precision("0.70", "0.20", precision=4), result)
        print()
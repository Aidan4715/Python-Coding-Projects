# Laboratory 5

## Laboratory Objectives
1. Write Python code using any editor.
2. Execute the program from the command line.
3. Unit test the program.
4. Upload on Canvas for submission

## Program Instructions
1. Write a Python package with sub-packages, modules, and functions using arguments.  Use the following directory outline and module names (your first starting point should be a directory called `mathematics`):
     ```
	mathematics/
		__init__.py
		whoami.py
		numbers/
			__init__.py
			whoami.py
			series.py
			simple.py
               algebra.py
		geometry/
			__init__.py
			whoami.py
			rectangle.py
			circle.py
			cube.py
     ```

1. Create a `mathematics` package.
     1. Initialize the `__all__` variable to the `whoami` module.
     1. Create a `whoami` module.
          1. Create a function named `getname` which returns the `__name__` variable.
     1. Create a `numbers` sub-package.
          1. Initialize the `__all__` variable to the `whoami` and `series` modules.
          1. Create a `whoami` module.
               1. Create a function named `getname` which returns the `__name__` variable.
          1. Create a `series` module.
               1. Create a function named `sum` which receives a  parameter `my_list` and returns the sum of all the values in the list.
               1. Create a function named `average` which receives a  parameter `my_list` and returns the average of all the values in the list.
          1. Create a `simple` module.
               1. Create a function named `addition` which receives parameters `left` and `right` and returns left plus right.
               1. Create a function named `subtraction` which receives the parameters `left` and `right` and returns left minus right.
               1. Create a function named `multiplication` which receives the parameters `left` and `right` and returns left multiplied by right.
               1. Create a function named `division` which receives the  parameters `left` and `right` and returns left divided by right.
          1. Create `algebra` modules:
               1. Create a function `quadratic(a, b, c)` that takes in 3 values a, b, c
               2. Calculate the roots based on those 3 values. 
               3. Return the pair of roots as a tuple
     1. Create a `geometry` sub-package.
          1. Initialize the `__all__` variable to the `whoami`, `circle`, and `cube` modules.
          1. Create a `whoami` module.
               1. Create a function named `getname` which returns the `__name__` variable.
          1. Create a `rectangle` module.
               1. Create a function named `perimeter` which receives a parameters `length` and `width` and returns (2l + 2h).
               1. Create a function named `area` which receives a parameters `length` and `width` and returns (l * h).
          1. Create a `circle` module.
               1. Create a function named `circumference` which receives the parameter `radius` and returns (2 * pi * r).
               1. Create a function named `area` which receives the parameter `radius` and returns (pi * r * r).
               1. Create a function named `sphere` which receives parameter `radius` and return the volume of a sphere
          1. Create a `cube` module.
               1. Create a function named `surface_area` which receives the parameter `side` and returns (s * s * 6).
               1. Create a function named `volume` which receives the  parameter `side` and returns (s * s * s).







## Program Instructions test
1. All the functions should accept the weather dictionary data structure as follows:
     ```
	weather dictionary:
		key : datetime as string (formatted as YYYYMMDDhhmmss)
		value : readings dictionary

	readings dictionary
		for key : 't'
		value : temperature as integer

		for key : 'h'
		value : humidity as integer

		for key : 'r'
		value : rainfall as float
     ```
1. Create a `weather` module.
     1. Create a function named `read_data` which receives parameters `filename`.
          1. Check if `filename` doesn't exist, return an empty dictionary (*hint*: use `os.path.exists()` )
          2. Otherwise, open the filename in read mode and return a dictionary of the JSON decoded contents of the file.

     1. Create a function named `write_data` which receives parameter `data` and `filename`
          1. The function should open the filename in write mode and write the data into the file.

     1. Create a function named `max_temperature` which receives parameter `data`
          1. The function should return the key of the date that had the highest temperature.

     1. Create a function named `min_temperature` which receives parameter `data`
          1.  The function should return the key of the date that had the lowest temperature.

     1. Create a function named `max_humidity` which receives parameter `data`
          1.  The function should return the key of the date that had the highest humidity.

     1. Create a function named `min_humidity` which receives parameter `data`
          1.  The function should return and key of the date that had the lowest humidity.

     1. Create a function named `tot_rain` which receives  parameter `data` and `date`
          1. The function should return the sum of rainfall for all dictionary data where the key contains the date as YYYYMMDD.

	 1. Create a function named `heading` and return this string:
		` f'{"Date":25} {"Time":13} {"Temperature":18} {"Humidity"} {"Rain":>15}' `

     1. Create a function named `report` which receives parameter `data` and `key`
	 
          1. The function should return one single string that contains date, time, temperature, humidity, and rain. Use 
	`heading` function to align your formatting.
	
	To get the month name, you can import the builtin `calendar` module and use the `month_name` list . (i.e: `month_name[1] = January`)
	
     1. Create a function named `report_historical` which receives a keyword parameter `data`
          2. This function will return only one string that contains each date and time that have the highest/lowest temperature and humidity. 
		  3. The return string should also includes the heading.

1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     2. Import the `weather.py` module.
     3. Read and store `w.dat` file
     4. Use `report_historical` to get the date and time. Write those date and time into `output.txt`. Be sure to align the text probably (use `sample_output.txt` and `heading()` as reference)




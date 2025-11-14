# Laboratory 9

## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Flight Schedule which contains a list of flight schedule data.
1. Create a `flights.py` module to meet the following requirements:
     1. Define a class named `Flights`:  

          1. Define a member function named `__init__` to meet the following requirements:
               1. Take a self object as a positional parameter.
               1. Take a filename string as a positional parameter.
               1. Set a member variable `file` equal to the filename. 
               1. Set a member variable `flight_list` equal to an empty data list. Use name mangling to limit access
               1. Open the filename and load the JSON decoded contents to the empty data list.
               1. Cleanly manage the `FileNotFoundError` if the filename does not exist.

          1. Define a member function named `save_flight`:
               1. Take a `self` as parameter
               2. Take a `filename` string as a parameter. Set a default_value to `flights_list.json`
               3. The function will open the file with `filename` and write to the file as JSON encoded content

          1. Define a member function named `format_time`: 
               1. Take `self` as parameter
               1. Take a `flight_time`:string (HHMM) as keyword argument
               2. This function will convert the flight time format from HHMM to hh:mm am/pm. 
               3. Return the convert time as a string 
               Example: `format_time("1430") = "2:30pm"`
          
          1. Define a member function named `duration`
               1. Take `self` as parameter
               1. Take `departure_time`:string (HHMM), `arrival_time`:string (HHMM), `next_day`:string (Y/N) as keyword arguments
               2. This function will calculate the duration of flight time. Return the duration as string `"HH:MM"`. Remember to properly account of next day duration

          1. Define a member function named `format_flight`
               1. Take `self` as parameter
               2. Take `flight`:dict as keyword argument. `flight` will follow the structure provided in `flights.json`
               2. Return a formatted flight based on the example given below:
                    1. `"origin": 'LAX'`
                    2. `"destination": 'ORD'`
                    3. `"flight number": '123'`
                    4. `"departure": '2:35pm'`: departure time need to be reformat
                    5. `"arrival": '+11:35am'`: arrival time need to be reformat. Adding `+` in front of arrival time to indicate the flight will arrive the next day
                    6. `"duration": '2:02'`: hours:minutes

          1. Define a member function named `add_flight` to meet the following requirements:
               1. Take a `self` object as parameter.
               1. Take a `origin`:string as a keyword argument
               1. Take a `destination`:string as a keyword argument
               1. Take a `flight_number`: string as a keyword argument
               1. Take a `departure`:string (as HHMM) as a keyword argument
               1. Take a `next_day`:string (Y/N) as a keyword argument
               1. Take a `arrival`: string (as HHMM) as a keyword argument
               2. If either the `departure` or `arrival` is not in the proper format, return `False`
               3. Append the flight to `flight_list` variable and update `flights_list.json` with newly added flight
               *Note: See `flights.json` file to understand the structure of flights element*
          
          1. Define a member function named `get_flight` to meet the following requirements:
               1. Take a `self` object as positional parameter
               1. Take a `flight_number` as keyword parameter, set default value to `None`
               2. Return the formatted `flight` containing all infomation about the flight based on the given flight number
               3. Return `None` if no flight is found

         1. Define a member function named `get_all_flights` to meet the following requirements:
              1. Take `self` object as  parameter.
              2. Return a list of formatted flight schedule data
              
        1. Define a member function named `remove_flight`:
            1. Take `self` as parameter
            2. Take `flight_number` as keyword parameter
            3. Remove the flight based on the given flight number
     
1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Import the `flights` module.
     2. Declare a variable to hold a list of flights creating an instance object of the `Flights` class.
     6. Implement a menu within a loop with following choices:
          1. Add fight
          2. Get flight
          3. Get all flights
          4. Remove flight
          9. Exit the program
     7. Prompt the user for the menu choice.

1. Typical input and output for the program:
     ```
           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add fight
     2. Get flight
     3. Get all flights
     4. Remove flight
     9. Exit the program

     Enter menu choice: 1

     Enter origin: LAX
     Enter destination: ORD
     Enter flight number: 545
     Enter departure time (HHMM): 1230
     Enter arrival time (HHMM): 1640
     Is arrival next day (Y/N): N

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add fight
     2. Get flight
     3. Get all flights
     4. Remove flight
     9. Exit the program

     Enter menu choice: 1

     Enter origin: ORD
     Enter destination: CLE
     Enter flight number: 409
     Enter departure time (HHMM): 1733
     Enter arrival time (HHMM): 1857
     Is arrival next day (Y/N): N

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add fight
     2. Get flight
     3. Get all flights
     4. Remove flight
     9. Exit the program

     Enter menu choice: 1

     Enter origin: CLE
     Enter destination: IAD
     Enter flight number: 83
     Enter departure time (HHMM): 1953
     Enter arrival time (HHMM): 2119
     Is arrival next day (Y/N): N

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add fight
     2. Get flight
     3. Get all flights
     4. Remove flight
     9. Exit the program

     Enter menu choice: 1

     Enter origin: IAD
     Enter destination: LHR
     Enter flight number: 1
     Enter departure time (HHMM): 2200
     Enter arrival time (HHMM): 0530
     Is arrival next day (Y/N): Y

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add fight
     2. Get flight
     3. Get all flights
     4. Remove flight
     9. Exit the program

     Enter menu choice: 1

     Enter origin: LHR
     Enter destination: LAX
     Enter flight number: 2222
     Enter departure time (HHMM): 2355
     Enter arrival time (HHMM): 2201
     Is arrival next day (Y/N): Y

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add fight
     2. Get flight
     3. Get all flights
     4. Remove flight
     9. Exit the program

     Enter menu choice: 3

     ================== FLIGHT SCHEDULE ==================
     Origin Destination Number Departure  Arrival Duration
     ====== =========== ====== ========= ======== ========
     LAX    ORD            545   12:30pm   4:40pm     4:10
     ORD    CLE            409    5:33pm   6:57pm     1:24
     CLE    IAD             83    7:53pm   9:19pm     1:26
     IAD    LHR              1   10:00pm  +5:30am     7:30
     LHR    LAX           2222   11:55pm +10:01pm    22:06

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add fight
     2. Get flight
     3. Get all flights
     4. Remove flight
     9. Exit the program

     Enter menu choice: 9
     ```


    

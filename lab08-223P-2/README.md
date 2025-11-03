# Laboratory 8
    
## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Contact List which contains a dictionary of contacts that is stored on the hard drive and that can have contacts added, modified, or deleted.
1. Create a `contacts` module to meet the following requirements:
      1. Create a file named `contacts.py`.
      1. Define a class named `Contacts`.  
            1. Define a member function named `__init__` to meet the following requirements:
                  1. Take a `self` as a parameter.
                  2. Take a `filename` as a parameter.
                  3. Set a member variable `file` equal to the filename. Set the default value to `phonebook.json`
                  4. Set a member varialbe `dict` equal to an empty data dictionary.
                  5. Open the filename and load the JSON decoded contents to the empty data dictionary.
                  6. Cleanly manage the `FileNotFoundError` if the filename does not exist.
            1. Define a member function named `add_contact` to meet the following requirements:
                  1. Take a `self` as a parameter.
                  2. Take a `phone` as a parameter.
                  3. Take a `first_name` as a parameter.
                  4. Take a `last_name` as a parameter.
                  5. If the `phone` exists in the data dictionary, return the string `error`.
                  6. Add to the data dictionary in this format: 'phone': [first_name, last_name]
                  7. Sort the data dictionary in ascending order by last name, and then by first name, ignoring case.
                  8. Write the contents of the data dictionary to the filename that was set to the member variable.
                  9. Return the key:value pair that was added.
            1. Define a member function named `modify_contact` to meet the following requirements:
                  1. Take a `self` as a parameter.
                  2. Take a `phone` as a d parameter.
                  3. Take a `first_name` as a parameter.
                  4. Take a `last_name` as a parameter.
                  5. If the `phone` does not exists in the dictionary, return the string `error`.
                  6. Set the phone:[first_name, last_name'] key:value pair to the contact dictionary.
                  7. Sort the data dictionary in ascending order by last name, and then by first name, ignoring case.
                  8. Write the contents of the data dictionary to the filename that was set to the member variable.
                  9. Return the key:value pair that was modified.
            1. Define a member function named `delete_contact` to meet the following requirements:
                  1. Take a `self` as a parameter.
                  1. Take a `phone` as a  parameter.
                  2. If the phone does not exists in the dictionary, return the string `error`.
                  3. Remove the key:value pair with the key equal to phone.
                  5. Write the contents of the data dictionary to the filename that was set to the member variable.
                  6. Return the key:value pair with the key equal to phone.
            1. Define a member function named `send_message` to meet the following requirements:
                  1. Take a `self` as a parameter
                  2. Take a `phone` as a parameter
                  3. Take a `message` as a parameter
                  4. Take a `messagelog` as a parameter. set the default value to `message.txt`
                  5. If the phone does not exists, return `error`
                  6. Write the message into the `messagelog`. The format will be: `Sending to first_name last_name: *message*`. Ex: `Sending to John Long: Greetings, John`
               
1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Import the `contacts` module.
     2. Instantiate a `Contacts` object with any default filename. 
     3. Implement a menu within a loop with following choices:
          1. Add contact
          2. Modify contact
          3. Delete contact
          4. Print contact list
          5. Sending message
          6. Set contact filename
          7. Exit the program
     4. Prompt the user for the menu choice.
     5. Prompt the user for the information needed for the appropriate `Contacts` member function and call the function.
     6. Print out appropriate errors with function return values of `error`.


1. Typical input and output for the program:
     ```
           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Send message
     6. Set contact filename
     7. Exit the program

     Enter menu choice: 1

     Enter phone number: 7145551212
     Enter first name: Steve
     Enter last name: Jobs
     Added: Steve Jobs.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Send message
     6. Set contact filename
     7. Exit the program

     Enter menu choice: 1

     Enter phone number: 5625553333
     Enter first name: Bill
     Enter last name: Gates
     Added: Bill Gates.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Send message
     6. Set contact filename
     7. Exit the program

     Enter menu choice: 4

     ==================== CONTACT LIST ====================
     Last Name             First Name            Phone
     ====================  ====================  ==========
     Gates                 Bill                  5625553333  
     Jobs                  Steve                 7145551212  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Send message
     6. Set contact filename
     7. Exit the program

     Enter menu choice: 1

     Enter phone number: 7145551111
     Enter first name: Alpha
     Enter last name: Jobs
     Added: Alpha Jobs.

    

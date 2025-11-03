import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

class Test01_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: contacts.add_contact(id = '7145551212', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates'], '7145551212': ['Richard', 'Stallman']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.add_contact(id = '7145551212', first_name = 'Richard', last_name = 'Stallman')
        c = {}
        with open('t99.dat', 'r') as f:
            c = json.load(f)
        self.assertEqual(c, {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates'], '7145551212': ['Richard', 'Stallman']})
        remove_file('t99.dat')
        print()

class Test02_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: r = contacts.add_contact(id = '7145551212', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates'], '7145551212': ['Richard', 'Stallman']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.add_contact(id = '7145551111', first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(r, 'error')
        remove_file('t99.dat')
        print()

class Test03_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: contacts.modify_contact(id = '7145551111', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: filename t99.dat = {'5625553333': ['Bill', 'Gates'], '7145551111': ['Richard', 'Stallman']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.modify_contact(id = '7145551111', first_name = 'Richard', last_name = 'Stallman')
        c = {}
        with open('t99.dat', 'r') as f:
            c = json.load(f)
        self.assertEqual(c, {'5625553333': ['Bill', 'Gates'], '7145551111': ['Richard', 'Stallman']})
        remove_file('t99.dat')
        print()

class Test04_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: r = contacts.modify_contact(id = '7145559999', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: r = 'error' ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.modify_contact(id = '7145559999', first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(r, 'error')
        remove_file('t99.dat')
        print()

class Test05_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: contacts.delete_contact(id = '7145551111') *** EXPECT: filename t99.dat = {'5625553333': ['Bill', 'Gates']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.delete_contact(id = '7145551111')
        c = {}
        with open('t99.dat', 'r') as f:
            c = json.load(f)
        self.assertEqual(c, {'5625553333': ['Bill', 'Gates']})
        remove_file('t99.dat')
        print()

class Test06_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: r = contacts.delete_contact(id = '7145551111') *** EXPECT: r = 'error' ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.delete_contact(id = '7145559999')
        self.assertEqual(r, 'error')
        remove_file('t99.dat')
        print()

class Test07_Send_One_Message(unittest.TestCase):
    def test_send_one_message(self):
        message_log = 'testing.txt'
        message = "hello"
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')

        phone_number = '7145551111'
        first = contacts.dict[phone_number][0]
        last = contacts.dict[phone_number][1]
        r = contacts.send_message(phone_number, message, messagelog=message_log)

        with open(message_log, 'r') as f:
            content = f.readlines()
            self.assertEqual(content[0], f"Sending to {first} {last}: {message}\n")

        remove_file('t99.dat')
        remove_file(message_log)

class Test07_Send_Multiple_Message(unittest.TestCase):
    def test_send_multiple_message(self):
        message_log = 'testing.txt'
        message1 = "hello"
        message2 = "hi"
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')

        phone_number = '7145551111'
        first = contacts.dict[phone_number][0]
        last = contacts.dict[phone_number][1]
        contacts.send_message(phone_number, message1, messagelog=message_log)
        contacts.send_message(phone_number, message2, messagelog=message_log)

        with open(message_log, 'r') as f:
            content = f.readlines()
            self.assertEqual(content[0], f"Sending to {first} {last}: {message1}\n")
            self.assertEqual(content[1], f"Sending to {first} {last}: {message2}\n")

        remove_file('t99.dat')
        remove_file(message_log)
        

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

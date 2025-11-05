import json

class Contacts:

    def __init__(self, filename = 'phonebook.json'):
        self.file = filename
        dict = {}

        try:
            with open(self.file, "r") as f:
                self.dict = json.load(f)

        except FileNotFoundError:
            print(f"File  '{self.file}' does not exist or cannot be found. Restarting with an empty contact list.")
            self.dict = {}
    
    def add_contact(self, phone, first_name, last_name):

        if phone in self.dict:
            print("error")

        self.dict[phone] = [first_name, last_name]

        for names in self.dict.values():
            for names in self.dict.values():
                if ()




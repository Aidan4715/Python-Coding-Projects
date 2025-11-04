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


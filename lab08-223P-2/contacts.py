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

        self.dict = dict(
            sorted(
                self.dict.items(), key = lambda item: (
                    item[1][1].lower(), item[1][0].lower()
                )
            )
        )

        with open(self.file, 'w') as f:
            json.dump(self.dict, f, indent=4)

        return dict[phone]
        

        





        




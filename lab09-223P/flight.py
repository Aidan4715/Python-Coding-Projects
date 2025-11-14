import json

class Flights:
    def __init__(self, filename=None):
        self.file = filename
        self.__flight_list = []
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    self.__flight_list = json.load(f)
            except FileNotFoundError:
                pass
    
    def save_flight(self, filename="flights_list.json"):
        with open(filename, 'w') as f:
            json.dump(self.__flight_list, f, indent=2)
        
        if self.file and self.file != filename:
            with open(self.file, 'w') as f:
                json.dump(self.__flight_list, f, indent=2)
    
    def format_time(self, *, flight_time):
        hours = int(flight_time[:2])
        minutes = flight_time[2:]
        
        period = "am" if hours < 12 else "pm"
        
        if hours == 0:
            hours = 12
        elif hours > 12:
            hours -= 12
        
        return f"{hours}:{minutes}{period}"
    
    def duration(self, *, departure_time, arrival_time, next_day):
        dep_hours = int(departure_time[:2])
        dep_minutes = int(departure_time[2:])
        arr_hours = int(arrival_time[:2])
        arr_minutes = int(arrival_time[2:])
        
        dep_total = dep_hours * 60 + dep_minutes
        arr_total = arr_hours * 60 + arr_minutes
        
        if next_day.upper() == 'Y':
            arr_total += 24 * 60
        
        duration_minutes = arr_total - dep_total
        
        hours = duration_minutes // 60
        minutes = duration_minutes % 60
        
        return f"{hours}:{minutes:02d}"
    
    def format_flight(self, *, flight):
        formatted = {}
        formatted["origin"] = flight["origin"]
        formatted["destination"] = flight["destination"]
        formatted["flight number"] = flight["flight_number"]
        formatted["departure"] = self.format_time(flight_time=flight["departure"])
        
        arrival_formatted = self.format_time(flight_time=flight["arrival"])
        if flight["next_day"].upper() == 'Y':
            arrival_formatted = '+' + arrival_formatted
        formatted["arrival"] = arrival_formatted
        
        formatted["duration"] = self.duration(
            departure_time=flight["departure"],
            arrival_time=flight["arrival"],
            next_day=flight["next_day"]
        )
        
        return formatted
    
    def add_flight(self, *, origin, destination, flight_number, departure, next_day, arrival):
        if len(departure) != 4 or not departure.isdigit():
            return False
        if len(arrival) != 4 or not arrival.isdigit():
            return False
        
        dep_hours = int(departure[:2])
        dep_minutes = int(departure[2:])
        arr_hours = int(arrival[:2])
        arr_minutes = int(arrival[2:])
        
        if dep_hours > 23 or dep_minutes > 59:
            return False
        if arr_hours > 23 or arr_minutes > 59:
            return False
        
        flight = {
            "origin": origin,
            "destination": destination,
            "flight_number": flight_number,
            "departure": departure,
            "arrival": arrival,
            "next_day": next_day
        }
        
        self.__flight_list.append(flight)
        self.save_flight()
        
        return True
    
    def get_flight(self, *, flight_number=None):
        if flight_number is None:
            return None
        
        for flight in self.__flight_list:
            if flight["flight_number"] == flight_number:
                return self.format_flight(flight=flight)
        
        return None
    
    def get_all_flights(self):
        return [self.format_flight(flight=flight) for flight in self.__flight_list]
    
    def remove_flight(self, *, flight_number):
        for i, flight in enumerate(self.__flight_list):
            if flight["flight_number"] == flight_number:
                self.__flight_list.pop(i)
                self.save_flight()
                return
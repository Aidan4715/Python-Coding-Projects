import flights

def flight_header():
    print("\n================== FLIGHT SCHEDULE ===================")
    print("Origin Destination Number Departure  Arrival  Duration")
    print("====== =========== ====== ========= ======== =========")

def flight_display(flight):
    print(f"{flight['origin']:<6} {flight['destination']:<11} {flight['flight_number']:<6} {flight['departure']:>9} {flight['arrival']:>8} {flight['duration']:>8}")

def display_menu():
    print("\n      *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU\n")
    print("1. Add fight")
    print("2. Get flight")
    print("3. Get all flights")
    print("4. Remove flight")
    print("9. Exit the program")

def add_flight(flight_schedule):
    print()
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    flight_number = input("Enter flight number: ")
    departure = input("Enter departure time (HHMM): ")
    arrival = input("Enter arrival time (HHMM): ")
    next_day = input("Is arrival next day (Y/N): ")
    
    result = flight_schedule.add_flight(
        origin=origin,
        destination=destination,
        flight_number=flight_number,
        departure=departure,
        next_day=next_day,
        arrival=arrival
    )
    
    if not result:
        print("Invalid time format. Flight not added.")

def get_flight(flight_schedule):
    print()
    flight_number = input("Enter flight number: ")
    
    flight = flight_schedule.get_flight(flight_number=flight_number)
    
    if flight:
        print(f"\nOrigin: {flight['origin']}")
        print(f"Destination: {flight['destination']}")
        print(f"Flight Number: {flight['flight number']}")
        print(f"Departure: {flight['departure']}")
        print(f"Arrival: {flight['arrival']}")
        print(f"Duration: {flight['duration']}")
    else:
        print("Flight not found.")

def get_all_flights(flight_schedule):
    flights_list = flight_schedule.get_all_flights()
    
    if not flights_list:
        print("\nNo flights available.")
        return
    
    print("\n================== FLIGHT SCHEDULE ==================")
    print("Origin Destination Number Departure  Arrival Duration")
    print("====== =========== ====== ========= ======== ========")
    
    for flight in flights_list:
        origin = flight['origin']
        destination = flight['destination']
        number = flight['flight number']
        departure = flight['departure']
        arrival = flight['arrival']
        duration = flight['duration']
        
        print(f"{origin:<6} {destination:<11} {number:>6} {departure:>9} {arrival:>8} {duration:>8}")

def remove_flight(flight_schedule):
    print()
    flight_number = input("Enter flight number to remove: ")
    
    result = flight_schedule.remove_flight(flight_number=flight_number)
    
    if result:
        print("Flight removed successfully.")
    else:
        print("Flight not found.")

def main():
    flight_schedule = flights.Flights("flights_list.json")
    
    while True:
        display_menu()
        print()
        choice = input("Enter menu choice: ")
        
        if choice == '1':
            add_flight(flight_schedule)
        elif choice == '2':
            get_flight(flight_schedule)
        elif choice == '3':
            get_all_flights(flight_schedule)
        elif choice == '4':
            remove_flight(flight_schedule)
        elif choice == '9':
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()



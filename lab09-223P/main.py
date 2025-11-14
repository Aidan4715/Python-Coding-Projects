
def flight_header():
    print("\n================== FLIGHT SCHEDULE ===================")
    print("Origin Destination Number Departure  Arrival  Duration")
    print("====== =========== ====== ========= ======== =========")

def flight_display(flight):
    print(f"{flight['origin']:<6} {flight['destination']:<11} {flight['flight_number']:<6} {flight['departure']:>9} {flight['arrival']:>8} {flight['duration']:>8}")






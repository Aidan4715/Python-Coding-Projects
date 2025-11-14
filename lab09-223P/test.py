import unittest
from unittest.mock import patch

import flights

import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

class Test01_ADDFLIGHT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** FUNCTION CALL: f.add_flight(origin='XXX', destination='YYY', flight_number='9999', departure='0907', arrival='1509', next_day='Y')  
        
        *** EXPECT: flight == {'origin': 'XXX', 'destination': 'YYY', 'flight_number': '9999', 'departure': '9:07am', 'arrival': '+3:09pm', 'duration': '30:02'} ***
        """
        remove_file('f99.dat')
        f = flights.Flights('f99.dat')
        f.add_flight(origin='XXX',
                     destination='YYY',
                     flight_number='9999',
                     departure='0907',
                     arrival='1509',
                     next_day='Y')
        flight = f.get_flight(flight_number='9999')
        self.assertEqual(flight, {'origin': 'XXX', 'destination': 'YYY', 'flight_number': '9999', 'departure': '9:07am', 'arrival': '+3:09pm', 'duration': '30:02'})
        remove_file('f99.dat')
        print()

class Test02_ADDFLIGHT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** FUNCTION CALL: f.add_flight(origin='XXX', destination='YYY', flight_number='9999', departure='090a', arrival='150b', next_day='Y') 
        
        *** EXPECT: None ***
        THEN flight = f.get_flight()
        """
        remove_file('f99.dat')
        f = flights.Flights('f99.dat')
        f.add_flight(origin='XXX',
                     destination='YYY',
                     flight_number='9999',
                     departure='090a',
                     arrival='150b',
                     next_day='Y')
        flight = f.get_flight()
        self.assertEqual(flight, None)
        remove_file('f99.dat')
        print()

class Test03_DURATION(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** FUNCTION CALL: f.duration(departure_time='2300', arrival_time='0030', next_day='Y')  
        
        *** EXPECT: '1:30' ***
        """
        f = flights.Flights()
        duration = f.duration(departure_time='2300', arrival_time='0030', next_day='Y')
        self.assertEqual(duration, '1:30')
        print()

class Test04_FORMATFLIGHT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** FUNCTION CALL: f.format_flight(flight={'origin': 'AAA', 'destination': 'BBB', 'flight_number': '1234', 'departure': '2200', 'arrival': '0100', 'next_day': 'Y'})  
        
        *** EXPECT: {'origin': 'AAA', 'destination': 'BBB', 'flight_number': '1234', 'departure': '10:00pm', 'arrival': '+1:00am', 'duration': '3:00'} ***
        """
        f = flights.Flights()
        flight = f.format_flight(flight={'origin': 'AAA',
                                        'destination': 'BBB',
                                        'flight_number': '1234',
                                        'departure': '2200',
                                        'arrival': '0100',
                                        'next_day': 'Y'})
        self.assertEqual(flight, {'origin': 'AAA', 'destination': 'BBB', 'flight_number': '1234', 'departure': '10:00pm', 'arrival': '+1:00am', 'duration': '3:00'})
        print()

class Test05_FORMATTIME(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** FUNCTION CALL: f.format_time(flight_time='0000')  
        
        *** EXPECT: '12:00am' ***
        """
        f = flights.Flights()
        time = f.format_time(flight_time='0000')
        self.assertEqual(time, '12:00am')
        print()

class Test06_GETALLFLIGHTS(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** FUNCTION CALL: f.get_all_flights()  
        
        *** EXPECT: [{'origin': 'CCC', 'destination': 'DDD', 'flight_number': '5678', 'departure': '1:15pm', 'arrival': '4:45pm', 'duration': '3:30'},
                     {'origin': 'EEE', 'destination': 'FFF', 'flight_number': '6789', 'departure': '8:00am', 'arrival': '10:00am', 'duration': '2:00'}] ***
        """
        remove_file('f99.dat')
        f = flights.Flights('f99.dat')
        f.add_flight(origin='CCC',
                     destination='DDD',
                     flight_number='5678',
                     departure='1315',
                     arrival='1645',
                     next_day='N')
        f.add_flight(origin='EEE',
                     destination='FFF',
                     flight_number='6789',
                     departure='0800',
                     arrival='1000',
                     next_day='N')
        all_flights = f.get_all_flights()
        self.assertEqual(all_flights, [{'origin': 'CCC', 'destination': 'DDD', 'flight_number': '5678', 'departure': '1:15pm', 'arrival': '4:45pm', 'duration': '3:30'},
                                       {'origin': 'EEE', 'destination': 'FFF', 'flight_number': '6789', 'departure': '8:00am', 'arrival': '10:00am', 'duration': '2:00'}])
        remove_file('f99.dat')
        print()

class Test07_GETFLIGHT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 *** FUNCTION CALL: f.get_flight(flight_number='1234')  
        
        *** EXPECT: {'origin': 'GGG', 'destination': 'HHH', 'flight_number': '1234', 'departure': '11:30am', 'arrival': '1:30pm', 'duration': '2:00'} ***
        """
        remove_file('f99.dat')
        f = flights.Flights('f99.dat')
        f.add_flight(origin='GGG',
                     destination='HHH',
                     flight_number='1234',
                     departure='1130',
                     arrival='1330',
                     next_day='N')
        flight = f.get_flight(flight_number='1234')
        self.assertEqual(flight, {'origin': 'GGG', 'destination': 'HHH', 'flight_number': '1234', 'departure': '11:30am', 'arrival': '1:30pm', 'duration': '2:00'})
        remove_file('f99.dat')

class Test08_REMOVEFLIGHT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 *** FUNCTION CALL: f.remove_flight(flight_number='4321')  
        
        *** EXPECT: None ***
        """
        remove_file('f99.dat')
        f = flights.Flights('f99.dat')
        f.add_flight(origin='III',
                     destination='JJJ',
                     flight_number='4321',
                     departure='1400',
                     arrival='1600',
                     next_day='N')
        f.remove_flight(flight_number='4321')
        flight = f.get_flight(flight_number='4321')
        self.assertEqual(flight, None)
        remove_file('f99.dat')
        print()
if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

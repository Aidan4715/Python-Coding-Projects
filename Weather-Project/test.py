import unittest
import os
import weather

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

data = {
    "20210203075501": {"t": 55, "h": 87, "r": 0}, 
    "20210203090602": {"t": 63, "h": 84, "r": 1}, 
    "20210203102903": {"t": 71, "h": 79, "r": 0.6}, 
    "20210203125504": {"t": 72, "h": 69, "r": 0.3}, 
    "20210203183905": {"t": 59, "h": 75, "r": 0.1}
    }
class Test01_weather_read_data_errorhandle(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 **** FUNCTION CALL: weather.read_data(filename='test.dat') *** EXPECT: {} ***
        """
        remove_file('test.dat')
        r = weather.read_data(filename='test.dat')
        self.assertEqual({}, r)
        remove_file('test.dat')

        print()

class Test02_weather_write_data(unittest.TestCase):
    def test_list_int(self):

        remove_file('test.dat')
        weather.write_data(data="20210203075501", filename='test.dat')
        r = weather.read_data(filename='test.dat')
        self.assertEqual(20210203075501, r)
        remove_file('test.dat')
        print()

class Test03_max_temperature(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 **** FUNCTION CALL: weather.max_temperature(data)*** EXPECT: "20210203125504" ***
        """
        r = weather.max_temperature(data)
        self.assertEqual("20210203125504", r)
        print()

class Test04_min_temperature(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 **** FUNCTION CALL: weather.min_temperature(data)***
        """
        r = weather.min_temperature(data)
        self.assertEqual("20210203075501", r)
        print()

class Test05_max_humidity(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test 05 *** FUNCTION CALL: weather.max_temperature(data)
        """
        r = weather.max_humidity(data)
        self.assertEqual("20210203075501",r)
        print()

class Test06_min_humidity(unittest.TestCase):
    def test_list_int(self):
        r = weather.min_humidity(data)
        self.assertEqual("20210203125504",r)
        print()

class Test07_total_rain(unittest.TestCase):
    def test_list_int(self):
        r = weather.tot_rain(data,"20210203")
        self.assertEqual(2.0,r)
        print()

class Test08_report(unittest.TestCase):
    def test_list_int(self):
        r = weather.report(data, "20210203183905")
        self.assertIn("February",r)

class Test09_contain_heading(unittest.TestCase):
        def test_list_int(self):
            r = weather.report_historical(data)
            self.assertIn(weather.heading(),r)

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

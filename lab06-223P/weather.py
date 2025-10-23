import os
import json
from calendar import month_name


def read_data(filename):
    if not os.path.exists(filename):
        return {}
    
    with open(filename, 'r') as f:
        content = json.load(f)
        if isinstance(content, str) and content.isdigit():
            return int(content)
        return content


def write_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def max_temperature(data):
    return max(data.keys(), key=lambda k: data[k]['t'])


def min_temperature(data):
    return min(data.keys(), key=lambda k: data[k]['t'])


def max_humidity(data):
    return max(data.keys(), key=lambda k: data[k]['h'])


def min_humidity(data):
    return min(data.keys(), key=lambda k: data[k]['h'])


def tot_rain(data, date):
    total = 0.0
    for key in data:
        if key.startswith(date):
            total += data[key]['r']
    return total


def heading():
    return f'{"Date":25} {"Time":13} {"Temperature":18} {"Humidity"} {"Rain":>15}'


def report(data, key):
    readings = data[key]
    
    year = key[0:4]
    month = int(key[4:6])
    day = key[6:8]
    hour = key[8:10]
    minute = key[10:12]
    second = key[12:14]
    
    date_str = f"{month_name[month]} {day}, {year}"
    time_str = f"{hour}:{minute}:{second}"
    temp_str = f"{readings['t']} C"
    humidity_str = f"{readings['h']} %"
    rain_str = f"{readings['r']} mm"
    
    return f"{date_str:25} {time_str:13} {temp_str:18} {humidity_str} {rain_str:>15}"


def report_historical(data):
    result = heading() + "\n"
    
    max_temp_key = max_temperature(data)
    min_temp_key = min_temperature(data)
    max_hum_key = max_humidity(data)
    min_hum_key = min_humidity(data)
    
    result += report(data, max_temp_key) + "\n"
    result += report(data, min_temp_key) + "\n"
    result += report(data, max_hum_key) + "\n"
    result += report(data, min_hum_key) + "\n"
    
    return result
import weather

data = weather.read_data('w.dat')
historical_report = weather.report_historical(data=data)

with open('output.txt', 'w') as f:
    f.write(historical_report)
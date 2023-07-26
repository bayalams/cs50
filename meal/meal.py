time = input('!')

def convert_hours(time):
    time = time.split(':')
    print(time)

    hours = float(time[0])
    minutes = float(time[1]) / 60

    return float(f'{hours},{minutes}')

convert_hours(time)
time = input('!')

def convert_hours(time):
    time = time.split(':')
    print(time)

    hours = int(time[0])
    minutes = float(time[1]) / 60

    s = hours + minutes
    #(f'{hours},{minutes}')
    print(s)
    return s


convert_hours(time)
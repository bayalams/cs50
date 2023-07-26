time = input('!')

def convert_hours(time):

    time = time.split(':')
    print(time)

    if time[0].isnumeric() and time[1].isnumeric() != True:
        print('error: values must be numerical. Words and letters are not supported.')
        exit(-1)

    hours = int(time[0])
    minutes = float(time[1]) / 60

    if not 0 <= hours <= 24:
        print('Value not supported. Hours must be between 0 and 24.')
        print(f'debug: {hours}')

    if not 0 <= minutes <= 1:
        print('Value not supported. Minutes must be between 0 and 1')
        print(f'debug: {minutes}')
        exit(-1)

    s = hours + minutes
    print(s)
    return s


convert_hours(time)
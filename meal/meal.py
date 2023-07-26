time = input('!')

def convert_hours(time):
    time = time.split(':')
    print(time)

    hours = int(time[0])
    minutes = float(time[1]) / 60

    if not 0 <= hours <= 24:
        print('Value not supported. Hours must be between 0 and 24.')
        exit(-1)

    if not 0 <= minutes <= 1:
        print('Value not supported. Minutes must be between 0 and 1')
        print('debug: )
        exit(-1)



    s = hours + minutes
    print(s)
    return s


convert_hours(time)
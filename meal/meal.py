time = input('!')

def convert_hours(time):
    time = time.split(':')
    print(time)

    hours = int(time[0])
    minutes = float(time[1]) / 60

    if not 0 < hours < 24 and 0 < minutes < 60:
        print('Value not supported. Hours must be between 0 and 24 and minutes must be between 0 and 60.')
        exit(-1)



    s = hours + minutes
    print(s)
    return s


convert_hours(time)
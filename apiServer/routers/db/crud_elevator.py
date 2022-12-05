from . import schemas
from datetime import datetime

def get_date():
    now = datetime.now()
    date_time = str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    return date_time

def going_up_elevator():
    date_time = get_date()
    f = open('elevator.txt', 'a')
    f.write('El elevador subio ' + date_time + '\n')
    f.close()
    return

def going_down_elevator():
    date_time = get_date()
    f = open('elevator.txt', 'a')
    f.write('El elevador bajo ' + date_time + '\n')
    f.close()
    return
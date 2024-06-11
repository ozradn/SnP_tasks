import time


def date_in_future(integer):
    if not type(integer) is int:
        return time.strftime("%d-%m-%Y %H:%M:%S")
    integer *= 86400
    future_time = time.localtime(time.time() + integer)
    return time.strftime("%d-%m-%Y %H:%M:%S", future_time)
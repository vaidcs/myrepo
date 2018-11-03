
#if current hour is <7 or >20 the return True else False

import datetime
hour = datetime.datetime.now().time().hour

def parrot_trouble(hour):
    if hour<7 or hour>20:
        return True
    else:
        return False

rt = parrot_trouble(hour)
print(rt)

# The parameter weekday is True if it is a weekday, and the
# parameter vacation is True if we are on vacation. We sleep in if
# it is not a weekday or we're on vacation. Return True if we
# sleep in.
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

import datetime
weekday = datetime.datetime.now().weekday()

def sleep_in(weekday, vacation):
    if vacation == 1:
        return True
    elif vacation == 0:
        if weekday ==5 or weekday ==6:
            # can sleep on
            return True
        else:
            # cant sleep on
            return False
    else:
        print("Wrong input")

vacation = int(input("Are You On Vacation, press"
                 "\n1 for yes"
                 "\n0 for no"))

rt = sleep_in(weekday,vacation)
print(rt)
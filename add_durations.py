# This function has the following algorithm:
#
# Convert each input duration to seconds
# Add all seconds
# Convert all the seconds to HH:MM:SS
# Return the result
#

# Importing floor and reduce
from math import floor
from functools import reduce

def add_time(ds):
    # Converting durations to seconds
    sec = sum([reduce(lambda x, y: int(x)*60 + int(y), d.split(':')) for d in ds])

    # Converting seconds to HH:MM:SS
    time = [floor(sec / 3600), floor(sec / 60) % 60, sec % 60]
    time = [("00" + str(t))[-2:] for t in time]
    
    # Return HH:MM:SS
    return ':'.join(time)


# List of inputs
inputs = [
    "3:13:45",
    "2:35:04",
    "1:17:37",
    "2:48:14",
    "1:48:49",
    "3:38:22",
    "2:26:56",
    "4:02:48",
    "1:54:08",
    "2:07:34"
]

# Print result
result = add_time(inputs)
print(result)

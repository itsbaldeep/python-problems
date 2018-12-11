import math

# Days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# get day function
def get_day(month, date, year):

    # Doomsdays in the year
    # 4 Jan and 29 Feb if it's a leap year
    doomsdays = [-1, 4 if year % 4 is 0 else 3 , 29 if year % 4 is 0 else 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    # Getting the century index
    # Initializing the main index
    c = math.floor(year / 100) % 4
    index = 0 if c is 1 else 5 if c is 2 else 3 if c is 3 else 2

    # Adding the alogithm logic to main index
    # Quotient by 12, It's remainder and It's quotient by 4
    index += math.floor((year % 100) / 12)
    index += (year % 100) % 12
    index += math.floor(((year % 100) % 12) / 4)

    # Finding the current date through closest doomsday
    index += date
    index -= doomsdays[month]

    # Returning the index converted to day
    return days[index % 7]


# Example - November 15, 2018
result = get_day(11, 15, 2018)
print(result)
# Prints Thursday

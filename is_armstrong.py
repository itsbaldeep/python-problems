def is_armstrong(num):
    sum = 0 # Variable representing sum of cubes
    num = str(num) # Converting input to string
    for i in range(0, len(num)): sum += int(num[i])**3 # Loop each digit and add their cubes
    return sum is int(num) # Returning a boolean val


result = is_armstrong(153)
print(result)

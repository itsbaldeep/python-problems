len = 15

# Let an empty list representing the series
f = [0] * len

# Base cases are 0, 1, ...
# So put the first element of list as 0
# Second element as 1
f[0] = 0
f[1] = 1

# For loop given number of times
# In every iteration, current element is sum of previous two
for i in range(2,len): f[i] = f[i - 1] + f[i - 2]

# Now simply print the list as comma and space seperated numbers
print(f)

# It prints the fibonacci series upto 15

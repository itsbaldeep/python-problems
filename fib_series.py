# Length of the list
n = 15

# Base cases are 2 (0 and 1)
# Remaining cases are n - 2 (0 for now)
f = [0, 1] + [0] * (n - 2)

# Loop through the list
# Set every element to be the sum of previous two
for i in range(2, n): f[i] = f[i - 1] + f[i - 2]

# Now just print the list
print(f)

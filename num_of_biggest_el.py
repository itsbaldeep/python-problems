list = [1,3,2,4,3] # A list with potentially more than one largest value

# Check for each value if it's the max
# Gives back a list of indeces for true values
# Print the length of that list
print(len([i for i, j in enumerate(list) if j is max(list)]))

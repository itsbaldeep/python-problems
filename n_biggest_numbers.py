# This program returns n number of biggest elements from a list
# Complexity is O(nm), where m is length of the list
# Can work with: str, float, int both -ve and +ve

# Parameters: (list, int)
# Return: str, float, int, list


def n_max(input_list, n):
    if n > len(input_list):  # Error if n value is bigger
        return "Error: n value is bigger than length of the list"

    # Main logic
    output_list = []  # Let a list to be returned
    for _ in range(n):  # Loop n number of times
        biggest = input_list[0]  # Let biggest be first value
        for j in range(len(input_list)):  # Loop through list
            if input_list[j] > biggest:  # If current value is bigger
                biggest = input_list[j]  # Then that's biggest
        output_list.append(biggest)  # Add that to output list
        input_list.remove(biggest)  # Remove that from input_list
    return output_list if len(output_list) > 1 else output_list[0]


# 3 Examples
result_1 = n_max([0, 0, -100, -2, -3, -1], 3)
result_2 = n_max([100, -100, 0, 20, 30], 2)
result_3 = n_max([1, 2, 3, 4, 5, 10], 1)
print(result_1)  # [0, 0, -1]
print(result_2)  # [100, 30]
print(result_3)  # 10

# Errors
result_err = n_max([19, 10, 40], 4)
print(result_err)  # Error

# Floating point numbers
result_float = n_max([0.1, -9.1, 8.33], 2)
print(result_float)  # [8.33, 0.1]

# Strings
result_str = n_max(['a', 'c', 'b', 'b'], 2)
print(result_str)  # ['c', 'b']

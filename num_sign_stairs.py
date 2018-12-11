# Let a function stairs which takes parameter n
# n here is representing the length and height of stairs

def stairs(n):
  # Reversed for loop from n down to 0
  for i in range(n, 0, -1):
    # Empty Space is repeated lesser and lesser times each loop
    # Number Sign is repeated more and more times each loop
    print(" "*(i - 1) + "#"*(n - i + 1))
  # Print empty space and number sign each loop


# Call the function with argument of any number
stairs(5)

# It prints the stairs with length of given argument

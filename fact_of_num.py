# Let a function named factorial which has a parameter n

def factorial(n):
  # When parameter is 0 or less, we return 1
  if (n <= 0): return 1
  # When paramter is more than 0
  # Return n times factorial of previous integer
  return n * factorial(n - 1)
  # This is called Recursion


# Call the factorial function with any integer argument
print(factorial(4))

# It gives the factorial of the passed argument

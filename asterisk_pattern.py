def ast_pattern(n=3, up=False):
    # Draw the pattern facing up
    if up:
        # Looping from 0 to n
        for i in range(n):
            # This statement works on any row, given total rows
            print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # Draw the pattern facing down
    else:
        # Looping from n to 0
        for i in range(n - 1, 0, -1):
            # Same statement as above
            print(' ' * (n - i - 1) + '*' * (2 * i + 1))


# Taking users input for row count
n = int(input('Enter the row count: '))

# First drawing downward facing pattern
ast_pattern(n, up=False)
# Then upward
ast_pattern(n, up=True)

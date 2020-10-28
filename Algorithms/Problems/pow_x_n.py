# Find X to the power of N, in log(n) time

# Note: This can be used in fast matrix exponentiation

### Recursive
# Recursive Function to calculate (x^y) in O(logy)
# Works with float x and negative y
def power(x, y):

    if (y == 0): return 1
    sqrt_x = power(x, int(y / 2))

    if (y % 2 == 0):
        return sqrt_x * sqrt_x
    else:
        if(y > 0): # Positive exp
            return x * sqrt_x * sqrt_x
        else: # Negative exp
            return (sqrt_x * sqrt_x) / x


### Iterative
# Iterative Function to calculate (x^y) in O(logy)
def power(x, y):

    # Initialize result
    res = 1

    while (y > 0):
        # If y is odd, multiply x with result
        if ((y & 1) == 1) :
            res = res * x

        # n is now even, so y = y/2
        y = y >> 1

        # Change x to x^2
        x = x * x

    return res


# Test Code
x = 3
y = 5

print("Power is ", power(x, y))

def nearest_price(n):
    # Calculate the lower and upper bound prices that end with 99
    lower = (n // 100) * 100 - 1
    if lower < 0:
        lower = 99
    upper = lower + 100
    
    # Determine which price is closer to the current price
    if n - lower < upper - n:
        return lower
    else:
        return upper

# Get the current price from the user
n = int(input())

# Print the nearest price that ends with 99
print(nearest_price(n))

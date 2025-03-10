n = int(input())

#get a bunch of prices
#want the most expensive books together to get the third most expensive free, etc
#we can sort them and group them that way
prices = []
for _ in range(n):
    prices.append(int(input()))

prices.sort()
prices.reverse()
total_price = 0
for i in range(n):
    if (i+1)%3 == 0:
        continue
    else:
        total_price += prices[i]

print(total_price)

import sys

prices = [7,1,5,3,6,4]

profit,min_value = 0, sys.maxsize

for price in prices:
  min_value = min(price,min_value)
  profit = max(profit, price - min_value)

print(profit)
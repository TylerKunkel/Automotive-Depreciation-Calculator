# Car Depreciation

print("Car Depreciation Calculator")
print()
print("=" * 67)
print()

amount = float(input("How much is your car worth?:\n"))

deppercent = int(input("What is the depreciation:\n"))
years = int(input("How many years?:\n"))

amount_left = amount

annual_depreciation = 0

print()
print("Initial amout = ", amount_left)
print()

for i in range(years):
    annual_depreciation = (deppercent * amount_left) / 100
    amount_left = amount_left - annual_depreciation

    print("After " + str(i + 1) +
          " years, your car is worth $%.2f " % amount_left)

print()

print("=" * 67)

print()

print("Final amount after " + str(i + 1) +
      " years of depreciation, is $%.2f " % amount_left)

foods_price = [('MoMo', 100), ('Pizza', 190), ('Frenchfry', 90)]
print("Original list of tuples:")
print(foods_price)
foods_price.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(foods_price)

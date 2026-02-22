def tuple_product(t):
    product = 1
    for num in t:
        product *= num
    return product

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

print("Product of tup1:", tuple_product(tup1))
print("Product of tup2:", tuple_product(tup2))

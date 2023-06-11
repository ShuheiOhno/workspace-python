def total_products(*values):
    result = 1
    for val in values:
        result *= val
    return result
print(total_products(12, 15, -1)) # -180
print(total_products(5, 7, 8, 2, 1, 15)) # 8400
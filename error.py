def calculate_total(price, tax):
    total = price + tax
    return total


item_price = 100
tax_rate = 10

result = calculate_total(item_price, tax_rate)
print("Total is", result)

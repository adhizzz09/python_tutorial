from functools import reduce

products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]

total_discounted_price = reduce(
    lambda acc, price: acc + price,
    map(
        lambda p: p[2] * 0.8,  # apply 20% discount
        filter(
            lambda p: p[1] == "Electronics",  # keep only Electronics
            products
        )
    ),
    0
)

print(total_discounted_price)

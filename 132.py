from functools import reduce

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]

# 1️⃣ Filter active customers
active_customers = filter(lambda c: c["active"], customers)


# 2️⃣ Extract and process valid purchases with tax
valid_purchases_with_tax = map(
    lambda c: map(
        lambda p: p * 1.10,
        filter(lambda p: p >= 100, c["purchases"])
    ),
    active_customers
)

# 3️⃣ Flatten and reduce to total
total_revenue = reduce(
    lambda acc, purchases: acc + sum(purchases),
    valid_purchases_with_tax,
    0
)

print(total_revenue)




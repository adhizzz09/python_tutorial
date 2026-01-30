def highest_selling(products):
    sales = {}
    for product, qty in products:
        sales[product] = sales.get(product, 0) + qty
    return max(sales, key=sales.get)
def main():
    sample_data = [("apple", 10), ("banana", 5), ("apple", 15), ("orange", 7)]
    result = highest_selling(sample_data)
    print(result)
if __name__ == "__main__":
    main()
    
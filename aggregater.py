sales = [("Pen", 10), ("Pencil", 5), ("Pen", 15)]
result = {}

for product, qty in sales:
    result[product] = result.get(product, 0) + qty

print(result)
def main():
    sentence = "Python is great and Python is easy"
    words = sentence.lower().split()  
    freq = {}
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    print(freq)
if __name__ == "__main__":
    main()
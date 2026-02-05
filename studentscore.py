students = [("Amit", [70, 80, 90]), ("Neha", [85, 90, 95])]
result = {}

for name, marks in students:
    result[name] = sum(marks) // len(marks)

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
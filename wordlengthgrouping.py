words = ["cat", "dog", "elephant", "bat"]
result = {}

for word in words:
    length = len(word)
    result.setdefault(length, []).append(word)

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
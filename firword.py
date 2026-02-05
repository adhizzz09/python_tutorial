words = ["cat", "dog", "elephant"]
result = {word: word[0] for word in words}

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
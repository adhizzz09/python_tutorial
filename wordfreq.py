import string

def word_frequency(sentence):
    words = sentence.lower().translate(
        str.maketrans("", "", string.punctuation)
    ).split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
def main():
    sample_sentence = "Hello world! Hello everyone."
    result = word_frequency(sample_sentence)
    print(result)
if __name__ == "__main__":
    main()
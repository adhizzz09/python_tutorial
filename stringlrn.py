def string_length_map(words):
    return {word: len(word) for word in words}
def main():
    sample_words = ["python", "ml", "ai"]
    result = string_length_map(sample_words)
    print(result)
if __name__ == "__main__":
    main()
def reverse_words(s):
    return (s.split()[::-1])

def main():
    sample_string="data science is fun"
    result=reverse_words(sample_string)
    print(result)
if __name__ == "__main__":
    main()
def key_check(d, key):
    return "Found" if key in d else "Not Found"
def main():
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    key_to_check = input("Enter the key to check: ")
    result = key_check(sample_dict, key_to_check)
    print(result)
if __name__ == "__main__":
    main()
    

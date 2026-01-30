def unique_characters(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return tuple(result)
def main():
    sample_string = "programming"
    result = unique_characters(sample_string)
    print(result)
if __name__ == "__main__":
    main()
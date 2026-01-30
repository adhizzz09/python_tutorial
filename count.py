def CountListElements(lst):
    output = {}
    for val in lst:
        if val in output:
            output[val] += 1
        else:
            output[val] = 1
    return output
def main():
    sample_list = [1, 2, 2, 3, 4, 4, 4, 5]
    result = CountListElements(sample_list)
    print(result)
if __name__ == "__main__":
    main()
    
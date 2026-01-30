def filter_even(nums):
    return [n for n in nums if n % 2 == 0]
def main():
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even(sample_list)
    print(result)
if __name__ == "__main__":
    main()
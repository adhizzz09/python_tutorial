def sum_of_tuples(lst):
    return [a + b for a, b in lst]
def main():
    sample_list = [(1, 2), (3, 4), (5, 6)]
    result = sum_of_tuples(sample_list)
    print(result)       
if __name__ == "__main__":
    main()
    
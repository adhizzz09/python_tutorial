def student_average(data):
    return {
        name.lower(): round(sum(marks) / len(marks), 2)
        for name, marks in data
    }
def main():
    sample_data = [("Alice", [85, 90, 78]), ("Bob", [70, 88, 92])]
    result = student_average(sample_data)
    print(result)
if __name__ == "__main__":
    main()
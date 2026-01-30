def tuple_to_dict(t):
    return dict(t)

def main():
    sample_tuple=(("a",1),("b",2))
    result=tuple_to_dict(sample_tuple)
    print(result)
if __name__ == "__main__":
    main()
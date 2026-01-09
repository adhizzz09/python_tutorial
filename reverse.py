def reversal_num():
    num=int(input("enter number:"))
    reversed_num=0
    original_num=num
    while(num>0):
        digit =num%10
    reversal_num = reversal_num * 10+ digit
    num=num // 10
    print(f"{original_num} is reversed"f"{reversal_num}")

    def main():
        reversal_num()

    if __name__ == "__main__":
        main()    
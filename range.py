
def checkeveodd():
    num=int (input("enter a number: "))
    if(num%2 ==0):
                print("the number is",num,"even")
    else:
        print("the number is "f"{num} is odd")

def eveoddrange():
    lower=int(input("enter a lower number: "))
    upper=int(input("enter a upper number: "))
    for num in range(lower,upper+1):
        if(num %2==0):
            print (f"{num} is even")
        else:
            print (f"{num} is odd")   
def main():
    eveoddrange()

if __name__ == "__main__":
    main()     


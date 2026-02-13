def UsingMap():
    employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]
    
    salaries = list(map(get_salary , employees))
    print(salaries)
    
    minsal = min(salaries)
    maxsal = max(salaries)
    filtersal = []
    for i in salaries:
            if i == minsal or i == maxsal:
                continue 
            filtersal.append(i)
            
    avg = sum(filtersal)/ len(filtersal)
    print(avg)
        
    
def get_salary(emp):
    return emp["salary"]
    

def demo():
        products = [
        ("Pen", 10),
        ("Bag", 50),
        ("Shoes", 60)
    ]
    
        price = list(map(get_price , products))
        print(price)
        
        inrprice = list(map(inr_price , price))
        print(inrprice)
        
        result = []
        for i in inrprice:
            if i <= 3000:
                continue
            result.append(i)
            
        print(result)
        
def get_price(product):
        return product[1]
def inr_price(price):
        return price * 83
    
def get_nor(word):
    lwrword = word.lower()
    wordss = lwrword.strip()
    return wordss

def stringexp():
    words = ["  Python ", "AI" ,"Machine ", "Data "]
    
    normalstr = list(map(get_nor, words))
    print(normalstr)
    
    for w in normalstr:
        if len(w)>5:
            print(w)
       
    



def main():
    #UsingMap()
    #demo()
    stringexp()
    
    
if __name__ == "__main__":
    main()
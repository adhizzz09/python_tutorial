class Book:
    def __init__(self,book_id,title,author,price,copies_avaiable):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.copies_avaiable = copies_avaiable

    def display_info(self):
        print("Book Id:",self.book_id)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        print("Copies Available:",self.copies_avaiable)
        print("-----------------------------")

    def issue_book(self,quantity):
        if quantity <= self.copies_available:
            self.copies_available -= quantity
            print(quantity,"copies issued successfully.")
        else:
            print("Not enough copies available")

    def return_book(self,quantity):
        self.copies_available += quantity
        print(quantity,"copies returned successfully.")
        def book_value(self):
            return self.price * self.copies_available


# Main Program

# Creating Book Objects
book1 = Book(101, "Python Programming", "Mark Lutz", 750, 5)
book2 = Book(102, "Data Structures and Algorithms", "Thomas H. Cormen", 1200, 3)
book3 = Book(103, "Machine Learning Basics", "Andrew Ng", 950, 4)

# List (Array) of Objects
library = [book1, book2, book3]

# Display All Books
print("Library Book Details")
print("=====================")
for book in library:
    book.display_book()

# Issue Copies
print("Issuing 2 copies of Python Programming")
book1.issue_book(2)

# Add Copies
print("Adding 3 copies to Machine Learning Basics")
book3.add_copies(3)

# Calculate Total Value of Library
total_value = 0
for book in library:
    total_value += book.book_value()

print("\nTotal Value of All Books in Library:", total_value)


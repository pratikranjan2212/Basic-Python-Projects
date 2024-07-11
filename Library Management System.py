class Library:
  def __init__(self):
    self.no_of_books = 0
    self.books = []

  def add_book(self,book):
    self.books.append(book)
    print(f"The book {book} has been added to the library.")
    self.no_of_books += 1
  
  def check_book(self):
    if self.no_of_books==len(self.books):
      print("The library has all the books.")
    else:
      print("The library does not have all the books.")

  def show_books(self):
    print("The books in the library are:")
    for book in self.books:
      print(book)

l1 = Library()
l1.add_book("Harry Potter")
l1.add_book("The Hobbit")
l1.add_book("The Lord of the Rings")
l1.add_book("The Da Vinci Code")
l1.add_book("The Great Gatsby")
l1.check_book()
l1.show_books()
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"
        
def main():
    library = []
    
    while True:
        print("\n--- Library Catalogue Menu ---")
        print("[1] Add Book  [2] View All  [3] Check Out  [4] Return  [5] Exit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.append(Book(title, author))
            print(f"Added {title} to the catalogue.")

        elif choice == '2':
            print("\n--- Current Catalogue ---")
            if not library: print("Catalogue is empty.")
            for i, book in enumerate(library):
                print(f"{i+1}. {book}")

        elif choice == '3':
            title = input("Enter the title to check out: ")
            found = False
            for book in library:
                if book.title.lower() == title.lower():
                    if book.checkout():
                        print(f"You have checked out '{book.title}'.")
                    else:
                        print(f"Sorry, '{book.title}' is already checked out.")
                    found = True
                    break
            if not found: print("Book not found.")

        elif choice == '4':
            title = input("Enter the title to return: ")
            for book in library:
                if book.title.lower() == title.lower():
                    book.return_book()
                    print(f"Thank you for returning '{book.title}'.")
                    break

        elif choice == '5':
            print("Closing system...")
            break

if __name__ == "__main__":
    main()       
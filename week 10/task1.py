# Base class for publications
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclass for books
class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

def main():
    # Create a magazine and a book
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    magazine.print_information()
    print()
    book.print_information()

if __name__ == "__main__":
    main()
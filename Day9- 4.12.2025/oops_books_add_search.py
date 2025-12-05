class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})

    def search_by_title(self, title):
        return [book for book in self.books if book['title'].lower() == title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if book['author'].lower() == author.lower()]

# Example usage:
library = Library()
library.add_book("Python Crash Course", "Eric Matthes")
library.add_book("1984", "George Orwell")

print(library.search_by_title("Python Crash Course"))
print(library.search_by_author("George Orwell"))

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"Libro {self.title} prestado")
        else:
            print(f"Libro {self.title} no disponible")
    
    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")

class User():
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow_book()
            self.borrowed_books.append(book)
        else:
            print(f"Libro {book.title} no disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"Libro {book.title} no está en la lista de prestados")

class Library():
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Libro {book.title} ha sido agregado a la lista de libros")

    def register_user(self, user):
        self.users.append(user)
        print(f"El Usuario {user.name} ha sido registrado")

    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"- Libro: {book.title} | Autor: {book.author}")

# Crear objeto Libro
print("Creando libros:")
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("El Aleph", "Jorge Luis Borges")

# Crear objeto Usuario
print("\nCreando usuario:")
user1 = User("Juan", "001")

# Crear Biblioteca
print("\nCreando Biblioteca:")
library = Library()
print("Agregando libro 1")
library.add_book(book1)
print("Agregando libro 2")
library.add_book(book2)
library.register_user(user1)

# Mostrar Libros
print("\nMostrando libros disponibles:")
library.show_available_books()

# Prestar libro
print("\nPrestar libro:")
user1.borrow_book(book1)
library.show_available_books()

# Devolver libro
print("\nDevolver libro:")
user1.return_book(book2)
library.show_available_books()

           

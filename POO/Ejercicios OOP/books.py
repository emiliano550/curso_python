class Book:

#Creamos nuestro constructor para inicializar la clase ----> __init__   
    def __init__(self,title, quantity, author, price):
        self.title = title 
        self.quantity = quantity 
        self.author = author
        self.price = price
#El término self en los atributos se refiere a las instancias correspondientes (objetos).

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

#libro1, libro2 y libro3 son objetos distintos de la clase Libro .
book1= Book('Book 1', 12, 'Author 1', 120)
book2= Book('Book 2', 18, 'Author 3', 220)
book3= Book('Book 3', 28, 'Author 3', 320)

print(book1)
print(book2)
print(book3)








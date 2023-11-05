class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
       print('Название:', self.title)
       print(f'Автор: {self.author}')
       print(f'Год издания {self.year}')


class Book(Publication):

    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f'ISBN: {self.isbn}')

class Magazine(Publication):

    def __init__(self, title, author, year, issuve_number):
        super().__init__(title, author, year)
        self.issuve_number = issuve_number

    def display(self):
        super().display()
        print(f'Номер журнала: {self.issuve_number}')

def info(obj):
    obj.display()

book1 = Publication('Название1', 'Автор1', 2015)
book2 = Book('Название2', 'Автор2', 2023, 543156743535)
book3 = Magazine('Название3', 'Автор3', 2077, 555777)

list = []
list.append(book1)
list.append(book2)
list.append(book3)
for i in list:
    info(i)
    print()

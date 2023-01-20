class publisher:
    def __init__(self):
        self.name="Khanna Publishing House"
    def display(self):
        print("publisher:",self.name)

class book(publisher):
    def __init__(self):
        self.title="Taming By Python Programming"
        self.author="Jeeva Jose"
    def display(self):
        super().__init__()
        super().display()
        print("Title:",self.title)
        print("Author:",self.author)

class python(book):
    def __init__(self):
        self.price="650"
        self.pages="346"
    def display(self):
        super().__init__() 
        super().display()
        print("Price:",self.price)
        print("No.of pages:",self.pages)


obj2=python()
print("Book Details are:\n")
obj2.display()

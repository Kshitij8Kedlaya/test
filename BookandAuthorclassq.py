class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def info(self):
        print("Name of the book:", self.title)
        print("Name of the author:", self.author )

bat = book("Harry Potter","J.K Rowling")
cat = book("Percy Jackson","Rick Riordan")
mat = book("The B.F.G","Roald Dahl")

bat.info()
cat.info()
mat.info()




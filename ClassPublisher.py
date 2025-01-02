class publisher():
    def __init__(self,name) :
        self.name=name
        
        
class book(publisher):
    def __init__(self, name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author

class python(book):
    def __init__(self, name, title, author, price,page_num):
        super().__init__(name, title, author)
        self.price=price
        self.pages=page_num
        
    def details(self):
        print(f"Publisher name : {self.name}")    
        print(f"Book Title : {self.title}")    
        print(f"Author : {self.author}")    
        print(f"Price : {self.price}")    
        print(f"Number of Pages : {self.pages}")


book1=python("ABC books","XYZ","Thahira","200","250")
book1.details() 
      
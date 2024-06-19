class User:

    def __init__(self, first_name, last_name):
        self.username = first_name
        self.lastname = last_name
    
    def sayName(self):
        print (self.username)
    
    def sayLastname (self):
        print (self.lastname)
    
    def sayBoth (self):
        print (self.username, self.lastname)
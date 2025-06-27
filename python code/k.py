class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def show(self):
        print("product name:",self.name)
        print("product price:",self.price)
        
obj = product("body spray",500)
obj.show()
    
    
    
    
    
    

  
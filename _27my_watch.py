# Python allows us to create class which we can import in other codes to stream line our code

class my_watch:
    
    def __init__(self, brand ,model, year ,price, in_production):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.in_production = in_production
    
    def elite_class(self):
        if self.price >= 15000:
            return True
        else :
            return False
    


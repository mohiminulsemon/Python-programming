class Phone: 
    manufactured = 'china'

    # def __init__(self):
    #     pass # pass is used in python for meaning empty like we use for(....){}  in c++ for empty body

    #constructor
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

my_phone = Phone('john', 'iphone', 1000)
print(my_phone.owner, my_phone.brand, my_phone.price)
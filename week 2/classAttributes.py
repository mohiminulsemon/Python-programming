class Shop:
    cart = [] # class attribute that is shared by all instances
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mehdi = Shop('mehdi')
mehdi.add_to_cart('phone')
print(mehdi.cart)

nisho = Shop('nisho')
nisho.add_to_cart('applephone')
print(nisho.cart)

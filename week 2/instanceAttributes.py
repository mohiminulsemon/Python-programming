class Shop:
    shoppingMall = 'basundhara'

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # cart is a instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('mehjabeen')
mehjabeen.add_to_cart('bread')
mehjabeen.add_to_cart('milk')
print(mehjabeen.cart)

nisho = Shop('nisho')
nisho.add_to_cart('watch')
nisho.add_to_cart('phone')
print(nisho.cart)
class Shopping: 
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        product = {
            'item': item,
            'price': price,
            'quantity': quantity
        }
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price ',total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'here is your change {extra}')


    def remove_from_cart(self,item):
        for product in self.cart:
            if product['item'] == item: 
                self.cart.remove(product)

swapan = Shopping('allan')
swapan.add_to_cart('alu',50,6)
swapan.add_to_cart('dim',12,24)
swapan.add_to_cart('rice',50,5)

print(swapan.cart)
swapan.checkout(1600)

swapan.remove_from_cart('rice')
print(swapan.cart)

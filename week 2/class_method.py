class Phone:
    phone = 'iphone'
    price = 1000
    def call(self): # default value should self, though there is no passing arguments
        print('calling')
    
    def send_msg(self, phone , msg): # it will receive two arguments phone and msg.
        # print(f'sending message to {phone} with msg {msg}' )
        text = f'sending message to {phone} with msg {msg}' 
        return text

my_phone = Phone() # making an object from class

print(my_phone)
print(my_phone.phone)

my_phone.call()

result = my_phone.send_msg('samsung', 'hello')
print(result)
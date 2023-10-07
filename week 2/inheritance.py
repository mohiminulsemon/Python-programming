# base class, parent class, common attribute/ functinality class
# child class/ derived class

class Gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin    

    def run(self):
        return f'Running gadget: {self.brand}'
    
class Laptop:
    def __init__(self,memory) -> None:
        self.memory = memory
    
    def coding(self):
        return f'Learning python programming'
    
class Phone(Gadget): # parent class inherited
    def __init__(self,dual_sim, brand, price, color, origin) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin) # initialize parent class attribute by calling child class constructor

    def __repr__(self) -> str:
        return f'Phone name: {self.brand}, price: {self.price}, color: {self.color}, origin: {self.origin}'
    
    def phone_call(self,number,text):
        return f'Sending msg to  {number} with text {text}'
    
class Camera:
    def __init__(self,pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        return f'Changing lens'
    

my_phone = Phone(dual_sim=True, brand='iPhone', price=1000, color='black', origin='China')
print(my_phone)
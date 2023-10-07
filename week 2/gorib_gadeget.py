class Laptop:
    def __init__(self,brand,price,color,memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'Learning python programming'
    
class Phone:
    def __init__(self,brand,price,color,dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def run(self):
        return f'phone tipa tipi koros kn'
    
    def phone_call(self,number,text):
        return f'Sending msg to  {number} with text {text}'
    
class Camera:
    def __init__(self,brand,price,color,pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        return f'Running camera: {self.brand}'
    def change_lens(self):
        return f'Changing lens'
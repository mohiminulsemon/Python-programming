class Company:
    def __init__(self,name,address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []

class Driver:
    def __init__(self,name,license,age) -> None:
        self.license = license
        self.name = name
        self.age = age

class Counter:
    pass
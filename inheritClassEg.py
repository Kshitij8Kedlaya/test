class car:
    def __init__(self,name,milage):
        self._name = name
        self.milage = milage
    
    def description(self):
        print(f"The {self._name} gives {self.milage} kmph")

class BMW(car):
    pass

class Audi(car):
    def description(self):
        super().description()
    def value(self):
        print("This is the audi class description") 

class Kia:
    def __init__(self,model):
        self.model = model
    def description(self):
        print(f"Model: {self.model}")
             

obj1 = Audi("Q7",70)
obj1.description()
obj1.value()
obj2 = BMW("S6",80)
obj2.description()
obj3 = Kia("Seltos")
obj3.description()



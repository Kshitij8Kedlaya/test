class employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    def hike(self):
        c = (self.salary/10) + self.salary
        print("Name:",self.name)
        print("Position:",self.position)
        print("Salary after 10% hike: ₹",c)

rat = employee("Sarah","Manager",50000)
bat = employee("David","President",250000)
sat = employee("Rachel","Engineer",30000)

rat.hike()
bat.hike()
sat.hike()





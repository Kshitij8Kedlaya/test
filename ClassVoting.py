class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def vote(self):
            a = self.age
            if a >= 18:
                print(f"{self.name} is eligible to vote")
            elif a < 18:
                b = 18-a
                print(f"Wait for {b} more years and {self.name} will be eligible to vote")


bat = person("Will",20)
cat = person("Lewis",13)
c = input("Name: ")
d = int(input("Age: "))
mat = person(c,d)

mat.vote()
bat.vote()
cat.vote()
    

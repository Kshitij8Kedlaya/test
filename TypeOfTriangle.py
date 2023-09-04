class triangle:
    def __init__(self,Side1,Side2,Side3):
        self.Side1 = Side1
        self.Side2 = Side2
        self.Side3 = Side3

    def type(self):   
        a = self.Side1
        b = self.Side2
        c = self.Side3
        if a == b == c:
            print("It is an Equilateral Triangle")
        elif a != b != c != a:
            print("It is a Scalene Triangle")
        else:
            print("It is an Isosceles Triangle")


trio = triangle(3,3,3)
trio.type()
tri = triangle(3,4,3)
tri.type()
three = triangle(4,5,6)
three.type()
[3:16 pm, 13/12/2019] \/|\/€|<: class abc:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _add_(self, pp):
        f = self.x + pp.x  # 2+6
        g = self.y + pp.y  # 3+7
        print(self.x)
        print(pp.x)
        print(self.y)
        print(pp.y)

        print(f + g)

    def _mul_(self, mm):
        a = self.x * mm.x
        b = self.y * mm.y
        print(a * b)

    def _sub_(self, sb):
        a = self.x - sb.x
        b = self.y - sb.y
        print(a - b)

    def _mod_(self, other):
        a = self.x % other.x
        b = self.y % other.y
        print(a % b)

    def _truediv_(self, divopr):
        a = self.x / divopr.x
        b = self.x / divopr.x
        print(a / b)
    def _pow_(self,poopr):
        a = self.x ** poopr.x
        b = self.y ** poopr.y
        print(a**b)

a = abc(127, 52)
b = abc(60, 7)

(a * b)
(a + b)
(a % b)
(a / b)
#print("The power opertor overloading is")
(a**b)
[3:16 pm, 13/12/2019] \/|\/€|<: Function overloading in python
[3:16 pm, 13/12/2019] \/|\/€|<: class Mathz:
    def addition(*var):
        sum = 0
        for x in var:
            sum = sum+x
        print(sum)
    
obj = Mathz
obj.addition(10,20)
obj.addition(10,20,50)
obj.addition(10,20,80,90)
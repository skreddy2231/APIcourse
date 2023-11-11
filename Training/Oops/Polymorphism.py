class Poly():

    a = 100
    def SelfTest(self):
        print("this is polymorphism class default function..", self.a)

    def addition(self, param1, param2):
        return print(f"Add/concatenate of values:", param1+param2)

p1 = Poly()

# one function, calling in many ways..<polymorphism>
p1.addition("Hello", "World")
p1.addition(20,30)
p1.addition(40.12, 30.16)
p1.addition([1,3,5], [2,4,6])  #list data
p1.addition(("py", "java", "perl"), (10,20,40))  # tuple data

class Cars():
    def cars_view(self):
        print("this is cars view function")

class Suzuki(Cars):
    def suzuki_view(self):
        print("this is suzuki class")


class grandparents():
    familyname = "Mr"
    def gp(self):
        print("this is grandparents class")
        print("Accessing function level variables:", self.familyname)

class parents(grandparents):
    def parent(self):
        print("this is parents class")

class children(parents):
    def ch(self):
        print("this is children class")

class newgen_child(children):
    def newgen(self):
        print("this is newgen_child class")


# Multiple inheritance - example
class CBSE():
    def centralboard(self):
        print("this is Central Board of Secondary Education data")

class IB():
    def ib(self):
        print("this is International Baccalaureate data")

class CISCE(CBSE, IB):
    def cisce(self):
        print("this is Council for the Indian School Certificate Examinations data")

class IGCSE():
    def igcse(self):
        print("this is International General Certificate of Secondary Education (IGCSE) Cambridge University")

class SB(CISCE,IGCSE):
    def stateboard(self):
        print("this is State Government Recognized Board data")


class KIA_Cars():
    def brand(self):
        print("this is manufactured by KIA")

class KIA_Carnival(KIA_Cars):
    def model1(self):
        print("this is KIA-Carnival high-end model1")

class KIA_Seltos(KIA_Cars):
    def model2(self):
        print("this is KIA-seltos model2")

class KIA_EV6(KIA_Cars):
    def model3(self):
        print("this is KIA-EV6 model3")

# single-level inheritance, create obj to child class
print("------------single-level inheritance------------------------\n")
cars_data = Suzuki()
cars_data.cars_view()
cars_data.suzuki_view()


# multi-level inheritance, create obj to low-level class.
print("------------multi-level inheritance------------------------\n")
family = newgen_child()
family.gp()
family.parent()
family.ch()
family.newgen()

# Multiple inheritance , create object.
print("------------multiple inheritance------------------------\n")
eduction_boards = SB()
eduction_boards.stateboard()
eduction_boards.igcse()
eduction_boards.cisce()
eduction_boards.ib()
eduction_boards.centralboard()


# Hierarchy inheritance (one parent, multiple child classes)
print("------------Hierarchy inheritance------------------------\n")
m1 = KIA_Carnival()
m2 = KIA_Seltos()
m3 = KIA_EV6()
m1.model1()
m2.model2()
m3.model3()

print("-------------END-----------------------\n")

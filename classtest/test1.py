class A:
    def addition(self, num1, num2):
        try:
            result = num1+num2
            print("addition test:",result)
        except ValueError as ve:
            print("error throws:", ve)
        except TypeError as te:
            print("Typeerror throws:", te)
        except Exception as ex:
            print("addition method found:", ex)

    def subtraction(self, num1, num2):
        try:
            result = num1 - num2
            print("subtraction test:", result)
        except TypeError as te:
            print("Typeerror throws:", te)
        except Exception as ex:
            print("subtraction method found:", ex)

    def multiple_modular(self, num1, num2):
        try:
            division = num1 / num2
            modulas = num1 % num2
            print("multiple_modular test:", division, " and :",modulas)
        except TypeError as te:
            print("multiple_modular throws:", te)
        except ZeroDivisionError as zd:
            print("division throws:", zd)
        except Exception as ex:
            print("subtraction method found:", ex)

# obj1 =A()
# obj1.multiple_modular(10,40)

# class B:
#     def search(self):
#         print("fhskhfks")
'''Wrapping up variables,methods in a single unit is called Encapsulation.
Public
private __  private variables can be accessible with in a class
protected _  protected variables can be accessible from any class through that <class> inheritance
'''

class Encap():
    try:
        __a = 10    # private
        _b = 20 # protected
        __c = 100
        _d = 200
        print("Get private variable:", __a)
        print("Get protected variable:",_b)

        def __init__(self, param1, param2):
            self.__param1 = param1
            self._param2 = param2
            print("this is default class function, will execute default, when class obj created", self.__param1, self._param2)

        def test2(self, p1, p2):
            self.__p1 = p1
            self._p2 = p2
            print("this is custom function, called explicitly>>",self.__p1, self._p2)
    except NameError as ne:
        print("NameError exception caught::\n",ne)



class Encap2(Encap):
    def demo(self):
        print("calling protected variables of parent class, by creating obj to the child class>>", self._param2)

e2 = Encap2(3,4)
e2.demo()
e2.test2("user", "test")
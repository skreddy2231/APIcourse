class feature2():
    print("created 'feature2' class")

    def __init__(self):
        print("this is default constructor from class feature2, called when obj created.")

    def amazon_search(self, a, b):  # here params are costructor and required params
        print(f"print given params a:{a} and b:{b}\n")
        return a + b


class feature3:
    print("I m feature3 class")
    def cart_items(self):  # here self param is positional args
        print("this is new feature3 from module2.py file")
        return "module2 file >> feature3 class >> cart_items function"

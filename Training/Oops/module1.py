class feature1():
    print("created 'feature1' class")
    var1 = 10
    def sample1(self):
        print("this is sample1 function from <feature1> class\n access variable var1:", self.var1)

    def secondtest(self, i, j):
        print(f"\n** this fn is Test1 py file i:{i} and j:{j}\n")
        return i * j

'''create object to class.
Note: can create N no.of objects to a given class.
'''
# f1 = feature1()

# call function by calling class object.
'''f1.sample1()
f1.secondtest(10,20)'''
names = ["Willem", "Ravi", "Tarun", "Alex", "ravi", "Tarun"]
for name in names:
    if name == "Tarun":
        break
    else:
        print("Not matched, checkign further..")
    print("Get name:", name)  # to print Tarun, by that time break stmt occured.


for name in names:
    if name == "Tarun":  # meaning, dont consider Tarun
        continue
    print("\nGet all name:", name)

for x in range(9):  # 0-8
    print(f"Range of val:'{x}'")
print("\n")

for y in range(3, 9):  # 3-8
    print(f"custom range:'{y}'")
print("\n")

for z in range(1, 20, 5):
    print(f"Increment range of values:'{z}'")
print("\n")

for i in range(1, 3):
    for j in range(4):
        print(i, "X", j, "=", i * j)
print("Done table!\n")

# define list directly
for ele in [10, 20, 300]:
    print(ele)
print("Get element", ele)

for ele2 in [200, "price"]:
    pass
print("Get pass element", ele2)
# Q: why pass stmt not resulted empty value
# https://www.w3schools.com/python/trypython.asp?filename=demo_for_pass


# arbitary argu & functions  (*args)
def emp_dept(*dept):  # undefined parameter
    print("emp dept list:", dept[2])


emp_dept("HR", "Engineer", "Architects", "Director")  # arguments


# keyword [key = value] args  [un-ordered keys]
def emp_ages(emp3, emp1, emp2):
    list1 = ["ages"]
    x = list1.append(emp3)
    x = list1.append(emp1)
    x = list1.append(emp2)
    print("emp name of HR department:", list1)


emp_ages(emp1=28, emp2=43, emp3=31)  # args passed like dictionaries

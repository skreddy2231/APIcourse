from datetime import date, datetime,timedelta

class Person:
   def __init__(self, name, dob, state, country):
        print("date variable type:", type(dob))
        # parameters = argument
        self.name = name
        self.dob = dob
        self.state = state
        self.country= country

   def format_age(self):
        d = date.today()
        age = d.year-self.dob.year
        return age

pobj = Person("testuser", date(2000,1,1), "kA", "India1")
print("name of person:", pobj.name)
#print("person age:", pobj.format_age())

# "01-0-1990"



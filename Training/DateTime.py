from datetime import date, timedelta
from datetime import datetime

#https://docs.python.org/3/library/datetime.html#datetime.timezone.utc
class DateTimeTests():
    def __init__(self):
        print(20*"-", "DATETIME Examples", 20*"-")

    def datetime_examples(self):
        d = date.today()
        t = datetime.now()
        print(30 * "*")
        print("current date:", d, " and day-name:", d.strftime("%A"))
        print("Get month:", d.month, " & other may return month-name:", d.strftime("%B"))
        print("Get only day:", d.year, "\n")

        # return weekday(), [Monday =0 ...sunday =6]
        # return isoweekday, [Monday =1 --> sunday = 7]
        print("Get no.of weekdays:", d.weekday(), " and weekend:", d.isoweekday(), "\n")
        get_day = date(2023, 1, 16).weekday() == 0
        get_day2 = date(2023, 1, 16).weekday() == 6
        print("Get day--->", get_day)
        print("Get day2,is this true? --->", get_day2)

        # strftime("%Y-%m-%d %H:%M:%S")  - string format time
        print("current date & time:", t)
        print("custom date format:", t.strftime("%d/%m/%y %H:%M:%S"))
        a = t.strftime("%d/%m/%y %H:%M:%S")
        print(type(a))  # type is 'str'
        print("strftime - string format time:", date.today().strftime("%A %d %B %Y"))

        # H - 24h format, I-12h format
        b = t.strftime("%d/%m/%y %I:%M:%S")
        datetime_12h = datetime.strptime(b, '%m/%d/%y %I:%M:%S')
        print("12h format:", datetime_12h)
        datetime_object = datetime.strptime(a, '%m/%d/%y %H:%M:%S')
        print(type(datetime_object))

    def subtract_daysfromsysdate(self):
        currentdate = date.today()
        days_back = 5
        pastdays = currentdate-timedelta(days_back)
        print("past days:", pastdays)

        yesterday = currentdate-timedelta(1)
        day_before = yesterday-timedelta(1)
        tomorrow = currentdate + timedelta(1)
        print("0000:", day_before, yesterday, tomorrow)
        c_date = date.today()
        if c_date.month==12:
            print("this month have 31 days...", date.today().month)
        else:
            print("this month have 30 days")

    def specificday(self,u_year):
        c_date = date(u_year, 1, 1)
        print(c_date.weekday())     # weekday starts (M - Saturday)
        c_date = c_date + timedelta(days = 6 - c_date.weekday())
        print("c_date:", c_date)
        while c_date.year == u_year:
            yield c_date
            c_date = c_date + timedelta(days=7)

        # print("Final C_date:", c_date)

    def specificday_wednesday(self,u_year):
        c_date = date(u_year, 1, 1)
        print(c_date.weekday())     # Sunday = 1, M =2, Saturday=7
        # c_date = c_date + timedelta(days = 7 - c_date.day)
        c_date = c_date + timedelta(days=4 - c_date.day)
        # print("c_date result:", c_date)
        while c_date.year == u_year:
            yield c_date
            c_date = c_date + timedelta(days=7)  # iterate next same day 9 calander 7 days)

dobj1 = DateTimeTests()
dobj1.subtract_daysfromsysdate()
dobj1.datetime_examples()
for i in dobj1.specificday_wednesday(2023):
    print("Get all (Wed) occurance days in a year::",i)
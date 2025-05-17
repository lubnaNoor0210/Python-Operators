import math
import datetime
import calendar

# ====MATH MODULE=====
print("Math Operations")
num = 25
print("square root of 5:", math.sqrt(num))
print("ceil of 1.9:", math.ceil(1.9)) # returns 2 as it is greater than or equal to (1.2)
print("floor of 2.4:", math.floor(2.4)) #returns the integer less than or equal to a number
print("Value of pi:", math.pi)

#======DATETIME MODULE=======
print("\n🕒 Date and Time:")
now = datetime.datetime.now()
print("current date and time:", now)
print("Today's date:", now.date())
print("current time:", now.time())
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)


#=======CALENDAR MODULE=========
# to get calender for month
cal = calendar.month(2025, 6)
print("here is the calender")
print(cal)
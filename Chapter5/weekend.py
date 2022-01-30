import datetime
weekDays = ("Monday", "Tuesday", "Wednesday", "Thurdsday", "Friday", "Saturday", "Sunday") #tuple containing day of the week
now = datetime.date.today() #sets a variable that retrieves the current date
dayOfWeek = now.weekday() #retrieve the day of the week which is an integer
today = weekDays[dayOfWeek] #subscript into weekDays using the dayOfWeek
daysToWeekend=6-dayOfWeek #calculate days until the weekend, set to variable
print(f"There are {daysToWeekend-1} days until the weekend") #prints days until the weekend
quotePrinted = "false" #flag to only print 1 quote in for loop
for left in weekDays[dayOfWeek:6]: #prints week days left until weekend with a quote
    if today =="Sunday" and quotePrinted == "false":
        print(left, "Sunday is the last weekend day!")
    elif today == "Monday" or today == "Tuesday" or today == "Wednesday" and quotePrinted =="false":
        print(left, "It's still early in the week....")
        quotePrinted ="true"
    elif today =="Thursday" and quotePrinted =="false":
        print(left, "So close to the weekend!")
        quotePrinted ="true"
    elif today =="Friday" and quotePrinted == "false":
        print(left, "ALRIGHT!! It's the weekend!")
        quotePrinted="true"
    else:
        print(left)


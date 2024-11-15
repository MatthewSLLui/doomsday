year = int(input("Enter year (1800 - 2199): "))
month = int(input("Enter month (between 1 - 12): "))
day = int(input("Enter day: "))

#Preliminary check if date input is valid or not.
valid_years = list(range(1800,2200))

valid_months = list(range(1,13))

valid_days = list(range(1,31))

if year not in valid_years or month not in valid_months or day not in valid_days:
    print("not valid input!")

#check if input year is leap

def leap_year_checker(year):

    is_leap = True
        
    if year % 400  == 0 and year % 100==0:
        pass

    elif year %100 != 0 and year %4 ==0:
        pass
    
    else:
        is_leap = False
    
    return is_leap


is_leap = leap_year_checker(year)

#Given the leap is leap or not, introduce extra constraints

def valid_date_checker(is_leap):

    if month == 2 and day > 29 and is_leap == True:
        return False
     
    elif month == 2 and day > 28 and is_leap == False:
        return False 
        
    elif (month == 4 or 6 or 9 or 11) and day == 31:
        return False

    else:
        return True


#print(valid_date_checker(is_leap))

# Find doomsday for the requested year

def doomsday (month):

    if is_leap == True:

        doomsdays = {1:4, 2:29, 3:14, 4:4 , 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}

    elif is_leap == False:

        doomsdays = {1:3, 2:28, 3:14, 4:4 , 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}
    return doomsdays

def anchorday (year):

    if year >=1800 and year <1900:
        anchor = 5
    elif year >=1900 and year < 2000:
        anchor = 3
    elif year >=2000 and year <2100:
        anchor = 2
    else:
        anchor = 0
    return anchor 

anchor_day = anchorday(year)

def doomsday_calculator(year,day,month):

    #extract last 2 digits of the year
    year_last2digits = year%100

    # how many 12's can you fit?
    multiples_of12 = year_last2digits//12
    
    # mod 12
    mod12 = year_last2digits%12

    # how many 4's can you fit in mod 12?

    count_of_fours = mod12//4


    total = anchor_day+ multiples_of12 + mod12 + count_of_fours
    day_of_the_week = total % 7 

    return day_of_the_week

day_of_the_week = doomsday_calculator(year,day,month)
#output is the day of week of all doomsday of that year
print(day_of_the_week)


#Now that you have found the doomsday given the year, find the doomsday on your month
def month_doomsday(month,day):
    doomsday_on_your_month = doomsday(month)
    x = doomsday_on_your_month[month]


    return (day-x + day_of_the_week)%7


#convert number to weekday:
#print(month_doomsday(month,day))


def output():
    weekday_dict ={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    return weekday_dict[month_doomsday(month,day)]


print(output())





    







   
import calendar 
import datetime
import random
from roman import toRoman
import os

def list_all_url():
    list_url=[]
    from_year= 1940
    today = datetime.date.today()
    to_year = today.year 
    for i in range(from_year, to_year+1):
        list_url.append(i)
        
    return list_url

def calculate_age(birth_date, current_date):
    # Calculation
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust for negative differences
    if days < 0:
        months -= 1
        days += get_days_in_month(birth_date.month, birth_date.year)
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def get_days_in_month(month, year):
    # Returns the number of days in a given month and year 
    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): 
            return 29  # Leap year
        else:
            return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November 
        return 30
    else:
        return 31
    
def calculate_age_final(date_of_birth, current_date):
    try:
        split_date_of_birth= date_of_birth.split('-')
        birth_day= int(split_date_of_birth[2])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[0])
        split_current_date= current_date.split('-')
        normal_current_date= f'{split_current_date[1]}-{split_current_date[2]}-{split_current_date[0]}'
        current_date= datetime.datetime.strptime(normal_current_date, '%m-%d-%Y').date()
        birth_date = datetime.date(birth_year, birth_month, birth_day)

        # Check if the birth date is valid
        if birth_date <= current_date:
            # Calculate age
        
            age_years, age_months, age_days = calculate_age(birth_date, current_date)
            return f"Your Age Is {age_years} Years, {age_months} Months, And {age_days} Days."
        else:
            return "Please enter a valid date of birth."
    except:
        return "Please enter a valid date of birth."
    
    
def result_template(result):
    search_categories = open('templates/zeodigital/index.html', "r", encoding="utf8").readlines()
    op= ''
    for search_categori in search_categories:
        op +=search_categori
        
    op= op.replace("﻿", '').replace('daycalculated', result).replace('<div class="boxanswer" style="display: none;">', '<div class="boxanswer" style="display: block;">')
    fp = open(f'templates/zeodigital/result/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
    
def get_all_months_year():
    filter_list=[]
    all_month_in_year=list(calendar.month_name)
    for all_month_in_ in all_month_in_year:
        if not all_month_in_.strip():
            continue
        filter_list.append(all_month_in_)
    return filter_list

def get_current_year():
    today = datetime.date.today()
    year = today.year
    return year

def calculate_age_final1(pageyear):
    try:
        split_date_of_birth= f'{pageyear}-{12}-{31}'.split('-')
        birth_day= int(split_date_of_birth[2])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[0])

        split_current_date= str(datetime.date.today()).split('-')
        normal_current_date= f'{split_current_date[1]}-{split_current_date[2]}-{split_current_date[0]}'
        current_date= datetime.datetime.strptime(normal_current_date, '%m-%d-%Y').date()
        birth_date = datetime.date(birth_year, birth_month, birth_day)

        # Check if the birth date is valid
        if birth_date <= current_date:
            # Calculate age
        
            age_years, age_months, age_days = calculate_age(birth_date, current_date)
            day_i= int(age_years) * 100
            return f"{pageyear} Was {age_years} Years, {age_months} Months, And {age_days} Days Ago Today. That's {day_i} days."
        else:
            return "Please enter a valid date of birth."
    except:
        return "Please enter a valid date of birth."
    

def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    output= '' 
    while number:
        div = number // num[i]
        number %= num[i]
 
        while div:
            output += sym[i]
            div -= 1
        i -= 1
    return output

def get_all_month_algo(pageyear):
    result= []
    for i in range(10, 131):
        current_year= pageyear + i
        first_str= f'How many years from {pageyear} to {current_year}?<title1>'
        second_str= f'The number of years from {pageyear} to {current_year} is {i} years.<title2>'
        result.append(first_str)
        result.append(second_str)
    return result

def all_dates_in_year(year):
    all_cre= []
    for month in range(1, 13): # Month is always 1..12
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            all_cre.append(f'{day} {month} {year}')
    return all_cre

def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))    
    dayNumber = calendar.weekday(year, month, day)
     
    # Modify days list to start with Sunday as 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
     
    return days[dayNumber]

def calculate_age_final2(pageyear, day, month):
    try:
        split_date_of_birth= f'{pageyear}-{month}-{day}'.split('-')
        birth_day= int(split_date_of_birth[2])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[0])

        split_current_date= str(datetime.date.today()).split('-')
        normal_current_date= f'{split_current_date[1]}-{split_current_date[2]}-{split_current_date[0]}'
        current_date= datetime.datetime.strptime(normal_current_date, '%m-%d-%Y').date()
        birth_date = datetime.date(birth_year, birth_month, birth_day)

        # Check if the birth date is valid
        if birth_date <= current_date:
            # Calculate age
        
            age_years, age_months, age_days = calculate_age(birth_date, current_date)
            day_i= int(age_years) * 100
            return f"{age_years} {age_months} {age_days}"
        else:
            return "Please enter a valid date of birth."
    except:
        return "Please enter a valid date of birth."
        
def credential_age(pageyear):
    January=[f'How old am i, If i was born in January, {pageyear}?<data0>']
    February=[f'How old am i, If i was born in February, {pageyear}?<data0>']
    March=[f'How old am i, If i was born in March, {pageyear}?<data0>']
    April=[f'How old am i, If i was born in April, {pageyear}?<data0>']
    May=[f'How old am i, If i was born in May, {pageyear}?<data0>']
    June=[f'How old am i, If i was born in June, {pageyear}?<data0>']
    July=[f'How old am i, If i was born in July, {pageyear}?<data0>']
    August=[f'How old am i, If i was born in August, {pageyear}?<data0>']
    September=[f'How old am i, If i was born in September, {pageyear}?<data0>']
    October=[f'How old am i, If i was born in October, {pageyear}?<data0>']
    November=[f'How old am i, If i was born in November, {pageyear}?<data0>']
    December=[f'How old am i, If i was born in December, {pageyear}?<data0>']
    today = datetime.date.today()
    year_sys = today.year
    all_month_in_year=list(calendar.month_name)
    all_data= all_dates_in_year(pageyear)
    for data_checker in all_data:
        split_checker= data_checker.split(' ')
        year= split_checker[2]
        month= int(split_checker[1])
        day= split_checker[0]
        confirm_month= all_month_in_year[month]
        brands = open(f"zeotech/static/content/{confirm_month}.txt", "r", encoding="utf8").readlines()
        days_of_the= findDay(data_checker)
        create_url=data_checker.replace(' ', '-')
        final_url= f'/dob/{create_url}'
        needed_data2= f'{day} {confirm_month} {year}, {days_of_the}<data1>{final_url}'
        result_against= calculate_age_final2(pageyear, day, month)
        if 'Please enter a valid date of birth.' == result_against:
            needed_data1= '	- - -<data2>'
            needed_data3= '	- - -<data3>'
        else:
            split_result_against= result_against.split(' ')
            spli_year= split_result_against[0]
            spli_month= split_result_against[1]
            spli_days= split_result_against[2]
            needed_data1= f'{spli_year} Years, {spli_month} Months, {spli_days} Days<data2>'
            
            min_year= int(year_sys) - int(pageyear)
            weeks= str(int(spli_days)/7)[0] 
            weeks_c= int(weeks) + min_year * 52
            days_c= int(spli_days) + 365 * min_year
            mints= 24*60* int(days_c)
            seconds= 60* int(mints)
            month_s= int(spli_month) + 12 * min_year
            
            needed_data3= f'or {month_s} months, or {weeks_c} weeks, or {days_c} days, or {mints} minutes, or {seconds} seconds<data3>$${brands[int(day)-1]}'
            
        if confirm_month == "January":
            January.append(needed_data2)
            January.append(needed_data1)
            January.append(needed_data3)
        elif confirm_month == "February":
            February.append(needed_data2)
            February.append(needed_data1)
            February.append(needed_data3)
        elif confirm_month == "March":
            March.append(needed_data2)
            March.append(needed_data1)
            March.append(needed_data3)
        elif confirm_month == "April":
            April.append(needed_data2)
            April.append(needed_data1)
            April.append(needed_data3)
        elif confirm_month == "May":
            May.append(needed_data2)
            May.append(needed_data1)
            May.append(needed_data3)
        elif confirm_month == "June":
            June.append(needed_data2)
            June.append(needed_data1)
            June.append(needed_data3)
        elif confirm_month == "July":
            July.append(needed_data2)
            July.append(needed_data1)
            July.append(needed_data3)
        elif confirm_month == "August":
            August.append(needed_data2)
            August.append(needed_data1)
            August.append(needed_data3)
        elif confirm_month == "September":
            September.append(needed_data2)
            September.append(needed_data1)
            September.append(needed_data3)
        elif confirm_month == "October":
            October.append(needed_data2)
            October.append(needed_data1)
            October.append(needed_data3)
        elif confirm_month == "November":
            November.append(needed_data2)
            November.append(needed_data1)
            November.append(needed_data3)
        elif confirm_month == "December":
            December.append(needed_data2)
            December.append(needed_data1)
            December.append(needed_data3)
    all_list_data=[[January], [February], [March], [April], [May], [June], [July], [August], [September], [October], [November], [December]]

    return all_list_data


def calculate_age_final4(date_of_birth, current_date):
    try:
        split_date_of_birth= date_of_birth.split('-')
        birth_day= int(split_date_of_birth[2])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[0])
        split_current_date= current_date.split('-')
        normal_current_date= f'{split_current_date[1]}-{split_current_date[2]}-{split_current_date[0]}'
        current_date= datetime.datetime.strptime(normal_current_date, '%m-%d-%Y').date()
        birth_date = datetime.date(birth_year, birth_month, birth_day)

        # Check if the birth date is valid
        if birth_date <= current_date:
            # Calculate age
        
            age_years, age_months, age_days = calculate_age(birth_date, current_date)
            return f"{age_years} {age_months} {age_days}"
        else:
            return "Please enter a valid date of birth."
    except:
        return "Please enter a valid date of birth."
        
def credential_over_all(date_of_birth, current_date):
    list_credent= []
    def format_one(date_of_birth):
        split_date_of_birth= date_of_birth.split('-')
        birth_day= int(split_date_of_birth[2])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[0])
        
        all_month_in_year=list(calendar.month_name)
        confirm_month= all_month_in_year[birth_month]
        data_checker= f'{birth_day} {birth_month} {birth_year}'
        
        days_of_the= findDay(data_checker)
        needed_data1= f'{birth_day} {confirm_month} {birth_year}, {days_of_the}'
        return needed_data1
    
    def format_two(date_of_birth):
        split_date_of_birth= date_of_birth.split('-')
        birth_day= int(split_date_of_birth[2])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[0])
        
        all_month_in_year=list(calendar.month_name)
        confirm_month= all_month_in_year[birth_month]
        data_checker= f'{birth_day} {birth_month} {birth_year}'
        
        days_of_the= findDay(data_checker)
        return days_of_the
    
    def format_three(age_in_years):
        # Calculate age in months
        age_in_months = age_in_years * 12
        
        # Calculate age in weeks
        age_in_weeks = int(age_in_years * 52.143)
        
        # Calculate age in seconds
        age_in_seconds = int(age_in_years * 365.25 * 24 * 60 * 60)
        
        age_in_days= int(age_in_years * 365)
        
        age_in_hours= int(age_in_years * 365 * 24)
        
        age_in_mint= int(age_in_years * 365 * 24 * 60)
        
        # Calculate age in milliseconds

        return age_in_months, age_in_weeks, age_in_seconds, age_in_days, age_in_hours, age_in_mint
    
    def format_four(date_of_birth):
        split_date_of_birth= date_of_birth.split('-')
        birth_day= int(split_date_of_birth[2])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[0])
        
        output= f'{toRoman(birth_month)}.{toRoman(birth_day)}.{toRoman(birth_year)}'
        return output
    
    def format_five(date_of_birth):
        split_date_of_birth= date_of_birth.split('-')
        day= int(split_date_of_birth[2])
        month= int(split_date_of_birth[1])
        
        
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "♒ Aquarius"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return "♒ Pisces"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "♒ Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "♒ Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "♒ Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "♒ Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "♒ Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "♒ Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "♒ Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "♒ Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "♒ Sagittarius"
        else:
            return "♒ Capricorn"
        
    def is_leap_year(year):
        split_date_of_birth= date_of_birth.split('-')
        year= int(split_date_of_birth[0])
        checker= calendar.isleap(year)
        if checker:
            return 'Yes'
        else:
            return 'No'
        
    def format_six(date_of_birth):
        split_date_of_birth= date_of_birth.split('-')
        birth_year= int(split_date_of_birth[0])

        BREATHS_PER_MINUTE = 16  # Average breaths per minute
        HEARTBEATS_PER_MINUTE = 75  # Average heartbeats per minute
        SMILES_PER_DAY = 15  # Average smiles per day
        SLEEP_PER_DAY = 8  # Average hours of sleep per day
        FOOD_PER_DAY = 1.5  # Average kilograms of food per day

        # Current year
        current_year = datetime.datetime.now().year

        # Calculate age
        age = current_year - birth_year

        # Calculate total breaths
        breaths = age * 365 * 24 * 60 * BREATHS_PER_MINUTE

        # Calculate total heartbeats
        heartbeats = age * 365 * 24 * 60 * HEARTBEATS_PER_MINUTE

        # Calculate total smiles
        smiles = age * 365 * SMILES_PER_DAY

        # Calculate total sleep
        sleep = age * 365 * SLEEP_PER_DAY

        # Calculate total food consumed
        food = age * 365 * FOOD_PER_DAY

        return f'{breaths} times', f'{heartbeats} times', f'{smiles} times', f'{sleep} hours', f'{food} kg'
    
    def format_seven(for_mat1, for_mat12, for_mat13, for_mat7, for_mat6):
        split_day= for_mat1.split(',')
        split_format1= f'How to write {split_day[0]} in roman numerals?'
        split_format2= f'The {split_day[0]} in roman numerals is {for_mat12}'
        split_format3= f'If I was born on {split_day[0]}, what is my Zodiac sign?'
        split_format4= f'If you were born on {split_day[0]} your Zodiac sign is {for_mat13}'
        split_format5= f'What day of the week was {split_day[0]}?'
        split_format6= f'The day of the week was {split_day[1]}.'
        split_format7= f'How many days ago was {split_day[0]}?'
        split_format8= f'There are {for_mat7} ago was {split_day[0]}.'
        split_format9= f'How many weeks ago was {split_day[0]}?'
        split_format10= f'There are {for_mat6}, {for_mat7} ago was {split_day[0]}.'
        
        commulation_k1= [split_format1, split_format2, split_format3, split_format4, split_format5, split_format6, split_format7, split_format8, split_format9, split_format10]
        return commulation_k1
        
        
        
        
    
    for_mat1= format_one(date_of_birth)
    for_mat2= format_one(current_date)
    split_for1= calculate_age_final4(date_of_birth, current_date).split(' ')
    year= split_for1[0]
    month= split_for1[1]
    day= split_for1[2]
    for_mat3= f'{year} Years, {month} Months, {day} Days'
    for_mat4= format_two(date_of_birth)
    age_in_months, age_in_weeks, age_in_seconds, age_in_days, age_in_hours, age_in_mint = format_three(int(year))
    for_mat5= f"{age_in_months} Months, {day} Days"
    for_mat6= f'{age_in_weeks} Weeks'
    for_mat7= f'{age_in_days} Days'
    for_mat8= f'{age_in_hours} Hours'
    for_mat9= f'{age_in_mint} Minutes.'
    for_mat10 = f'{age_in_seconds} Seconds'
    for_mat11= f'{month} Months, {day} Days'
    for_mat12= format_four(date_of_birth)
    for_mat13= format_five(date_of_birth)
    for_mat14= is_leap_year(date_of_birth)
    for_mat15, for_mat16, for_mat17, for_mat18, for_mat19= format_six(date_of_birth)
    list_credent1= format_seven(for_mat1, for_mat12, for_mat13, for_mat7, for_mat6)
    
    commulation_k= [for_mat1, for_mat2, for_mat3, for_mat4, for_mat5, for_mat6, for_mat7, for_mat8, for_mat9, for_mat10, for_mat11, for_mat12, for_mat13, for_mat14, for_mat15, for_mat16, for_mat17, for_mat18, for_mat19]
    list_credent += commulation_k
    list_credent += list_credent1
    
    return list_credent
    

def famous_people(date_of_birth):
    split_date_of_birth= date_of_birth.split('-')
    birth_day= int(split_date_of_birth[2])
    birth_month= int(split_date_of_birth[1])
    birth_year= int(split_date_of_birth[0])
    all_month_in_year=list(calendar.month_name)
    month_name= all_month_in_year[birth_month]
    brands = open(f"zeotech/static/content/{month_name}content.txt", "r", encoding="utf8").readlines()
    return brands[birth_day-1]
    
    


    
    

 

        



    
    
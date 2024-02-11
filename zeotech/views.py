from django.shortcuts import render
from django.http import HttpResponse
from .operation import *
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response):
    display= 'boxanswer'
    displays1= 'visibility_alo1'
    list_url= list_all_url()
    boxcredential=[]
    forms= CreateNewList()
    
    if response.method == "POST":
        date_of_birth = response.POST.get('mydateofbirth')
        current_date=  response.POST.get('currentdate')
        
        result= calculate_age_final(date_of_birth, current_date)
        display= 'boxanswer1'
        displays1= 'visibility_alo2'
        boxcredential= credential_over_all(date_of_birth, current_date)
        
        famouspeople= famous_people(date_of_birth)
       
        
        return render(response, "zeodigital/result/index.html", {
            'display_s': display,
            'display_s1': displays1,
            'side_list': list_url,
            'box_credential': boxcredential,
            'form': forms,
            'out_result': result,
            'famousypeople': famouspeople,
            'dateofbirth': date_of_birth,
             
        })
        
    return render(response, "zeodigital/index.html", {
        'display_s': display,
        'display_s1': displays1,
        'side_list': list_url,
        'box_credential': boxcredential,
        'form': forms,
        
    })
    
def index1(response):
    pageyear= '1960'
    currenyear= get_current_year()
    list_url= list_all_url()
    all_month= get_all_months_year()
    agemin= int(currenyear) - int(pageyear)
    daysage= agemin * 100
    resultage= calculate_age_final1(pageyear)
    romanru= printRoman(int(pageyear))
    resultdata= get_all_month_algo(int(pageyear))
    all_month_split= credential_age(int(pageyear))
    
    January=all_month_split[0][0]
    February=all_month_split[1][0]
    March=all_month_split[2][0]
    April=all_month_split[3][0]
    May=all_month_split[4][0]
    June=all_month_split[5][0]
    July=all_month_split[6][0]
    August=all_month_split[7][0]
    September=all_month_split[8][0]
    October=all_month_split[9][0]
    November=all_month_split[10][0]
    December=all_month_split[11][0]
    
    
    return render(response, "zeodigital/1960/index.html", {
        'side_list': list_url, 
        'all_month_year': all_month, 
        'current_year': currenyear, 
        'page_year': pageyear, 
        'age_min': agemin, 
        'days_age': daysage, 
        'result_age': resultage, 
        'roman_ru': romanru, 
        'result_data': resultdata, 
        'January_block': January, 
        'February_block': February, 
        'March_block': March, 
        'April_block': April, 
        'May_block': May, 
        'June_block':June, 
        'July_block': July, 
        'August_block': August, 
        'September_block': September, 
        'October_block': October, 
        'November_block': November, 
        'December_block': December
    })
    

def index2(response):
    date_of_birth= '1960-1-1'
    current_date= str(datetime.date.today())
    forms= CreateNewList()
    display= 'boxanswer1'
    displays1= 'visibility_alo2'
    list_url= list_all_url()
    boxcredential=[]
    result= calculate_age_final(date_of_birth, current_date)
    boxcredential= credential_over_all(date_of_birth, current_date)
    
    famouspeople= famous_people(date_of_birth)
    if response.method == "POST":
        date_of_birth = response.POST.get('mydateofbirth')
        current_date=  response.POST.get('currentdate')
        
        result= calculate_age_final(date_of_birth, current_date)
        display= 'boxanswer1'
        displays1= 'visibility_alo2'
        boxcredential= credential_over_all(date_of_birth, current_date)
        
        famouspeople= famous_people(date_of_birth)
        return render(response, "zeodigital/result/index.html", {
            'display_s': display,
            'display_s1': displays1,
            'side_list': list_url,
            'box_credential': boxcredential,
            'form': forms,
            'out_result': result,
            'dateofbirth': date_of_birth,
            'famousypeople': famouspeople
             
        })
        
    return render(response, "zeodigital/dob/1-1-1960/index.html", {
        'side_list': list_url, 
        'display_s': display, 
        'out_result': result, 
        'box_credential': boxcredential, 
        'display_s1': displays1, 
        'dateofbirth': date_of_birth, 
        'famousypeople': famouspeople
    })

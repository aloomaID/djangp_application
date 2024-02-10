import calendar 
import datetime
import random
from roman import toRoman
import os
import schedule
import time
import datetime

def create_pages_directory():
    sss=1
    format_page1= '''
def index<<2>>(response):
    pageyear= <<1960>>
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
    
    
    return render(response, "zeodigital/<<1960>>/index.html", {
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
    
    '''
    format_page2= '''
def index<<2>>(response):
    date_of_birth= '<<1960-1-1>>'
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
            'famousypeople': famouspeople
             
        })
        
    return render(response, "zeodigital/dob/<<1-1-1960>>/index.html", {
        'side_list': list_url, 
        'display_s': display, 
        'out_result': result, 
        'box_credential': boxcredential, 
        'display_s1': displays1, 
        'dateofbirth': date_of_birth, 
        'famousypeople': famouspeople
    })

    '''
    def how_arranged():
        brands = '''
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
            'famousypeople': famouspeople
             
        })
        
    return render(response, "zeodigital/index.html", {
        'display_s': display,
        'display_s1': displays1,
        'side_list': list_url,
        'box_credential': boxcredential,
        'form': forms,
        
    })
        '''
        Good = open("views.py", "w", encoding='utf-8-sig')
        Good.write(brands + "\n")
        Good.close()
        brands1= '''
from django.urls import path

from . import views

urlpatterns= [
    path("", views.index, name='index'),
        '''
        Good1 = open("urls.py", "w", encoding='utf-8-sig')
        Good1.write(brands1 + "\n")
        Good1.close()
        
    sitemaps = []
    sitemaps.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    def first_format_correction(format_page1, i, sss):
        save= format_page1.replace('<<1960>>', f'{i}').replace('index<<2>>', f'index{sss}')
        checker= save[:24].strip()
        brands = open("views.py", "r", encoding="utf8").read()
        if checker in brands:
            pass
        else:
            Good = open("views.py", "a", encoding='utf-8-sig')
            Good.write(save + "\n")
            Good.close()
            path='''
    path("year/<<1960>>/", views.index<<2>>, name='index<<2>>'),
            '''
            save_path= path.replace('<<1960>>', f'{i}').replace('index<<2>>', f'index{sss}')
            Good1 = open("urls.py", "a", encoding='utf-8-sig')
            Good1.write(save_path + "\n")
            Good1.close()
            
        return f'<url><loc>https://agecalculator.zeodigital.com/year/{i}</loc></url>'
        
    
    def second_format_correction(format_page2, url, sss):
        split_date_of_birth= url.split('-')
        birth_day= int(split_date_of_birth[0])
        birth_month= int(split_date_of_birth[1])
        birth_year= int(split_date_of_birth[2])
        reformate= f'{birth_year}-{birth_month}-{birth_day}'
        save= format_page2.replace('<<1-1-1960>>', f'{url}').replace('index<<2>>', f'index{sss}').replace('<<1960-1-1>>', reformate)
        checker= save[:28].strip()
        brands = open("views.py", "r", encoding="utf8").read()
        if checker in brands:
            pass
        else:
            Good = open("views.py", "a", encoding='utf-8-sig')
            Good.write(save + "\n")
            Good.close()
            path='''
    path("dob/<<1-1-1960>>/", views.index<<2>>, name='index<<2>>'),
            '''
            save_path= path.replace('<<1-1-1960>>', f'{url}').replace('index<<2>>', f'index{sss}').replace('<<1960-1-1>>', reformate)
            Good1 = open("urls.py", "a", encoding='utf-8-sig')
            Good1.write(save_path + "\n")
            Good1.close()
        return f'<url><loc>https://agecalculator.zeodigital.com/dob/{url}</loc></url>'
        
        
    def create_in_root(year, format_page2, sss):
        site_url= []
        for month in range(1, 13): # Month is always 1..12
            for day in range(1, calendar.monthrange(year, month)[1] + 1):
                url=f'{day}-{month}-{year}'
                sity= second_format_correction(format_page2, url, sss)
                site_url.append(f"{sity}")
                if '1-1-1960' == url:
                    sss +=1
                    continue
                try:
                    os.makedirs(f'templates/zeodigital/dob/{url}') 
                except:
                    pass
                infile = open("templates/zeodigital/dob/1-1-1960/index.html", 'r', encoding='utf8')
                s1 = infile.read()
                infile.close()
                
                fp = open(f'templates/zeodigital/dob/{url}/index.html', "w", encoding='utf-8-sig')
                fp.writelines(s1)
                fp.close()
                sss +=1
        return sss, site_url
    how_arranged()   
    from_year= 1940
    today = datetime.date.today()
    to_year = today.year
    for i in range(from_year, to_year+1):
        sss, site_url= create_in_root(i, format_page2, sss)
        sity= first_format_correction(format_page1, i, sss)
        sitemaps.append(sity)
        sitemaps += site_url
        if 1960 == i:
            sss +=1
            continue
        try:
            os.makedirs(f'templates/zeodigital/{i}') 
        except:
            pass
        infile = open("templates/zeodigital/1960/index.html", 'r', encoding='utf8')
        s1 = infile.read()
        infile.close()
        fp = open(f'templates/zeodigital/{i}/index.html', "w", encoding='utf-8-sig')
        fp.writelines(s1)
        fp.close()
        sss +=1
        
    sitemaps.append('</urlset>')
    try:
        os.makedirs('templates/zeodigital/sitemaps') 
        parent_dir5 = f"templates/zeodigital/sitemaps/sitemaps.xml"
        f = open(parent_dir5, "a", encoding='utf-8-sig', errors='replace')
        for site in sitemaps:
            f.write(site + '\n')
        f.close()
    except:
        pass
    closing= '''
def sitemaps(response):
    return render(response, "zeodigital/sitemaps/sitemaps.xml")

    '''
    Good = open("views.py", "a", encoding='utf-8-sig')
    Good.write(closing + "\n")
    Good.close()
    brands2= '''
]
    '''
    Good1 = open("urls.py", "w", encoding='utf-8-sig')
    Good1.write(brands2 + "\n")
    Good1.close()
    
schedule.every().day.at("11:48").do(create_pages_directory)

while True:
    schedule.run_pending()
    time.sleep(60)
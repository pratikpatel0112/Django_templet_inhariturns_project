import datetime as dt

def age(studDOB):
    today_date = dt.datetime.today()
    today_date_year = today_date.year
    birth_year = studDOB.year
    
    year_old = today_date_year - birth_year
    
    today_date_month = today_date.month
    birth_momth = studDOB.month
    month_old = today_date_month - birth_momth
    
    return (f"{year_old}year,{month_old}month")

''' 
to call the tis template filtar in template .. html file we need to register a function as a django filter in using 
django filter lybray as follow
'''

from django import template

register = template.Library()
register.filter('studage',age)
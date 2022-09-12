from django.shortcuts import render
import datetime as dt

# Create your views here.

studlist = [
    { 'studid': 1 , 'studname': 'ajay kumar', 'studDOB' : dt.datetime(2000,1,10),'studAddDate':dt.datetime(2005,6,1)},
    { 'studid': 2 , 'studname': 'rakesh sharma', 'studDOB' : dt.datetime(2001,2,9),'studAddDate':dt.datetime(2006,5,10)},
    { 'studid': 3 , 'studname': 'priya mohite ', 'studDOB' : dt.datetime(2000,3,8),'studAddDate':dt.datetime(2005,6,20)},
    { 'studid': 4 , 'studname': 'ram sharma', 'studDOB' : dt.datetime(2001,4,7),'studAddDate':dt.datetime(2005,6,30)},
    { 'studid': 5 , 'studname': 'poonam patil', 'studDOB' : dt.datetime(2000,5,6),'studAddDate':dt.datetime(2005,5,1)},
    { 'studid': 6 , 'studname': 'atul jain', 'studDOB' : dt.datetime(2001,6,5),'studAddDate':dt.datetime(2006,5,1)},
    { 'studid': 7 , 'studname': 'arun yadav', 'studDOB' : dt.datetime(2000,7,4),'studAddDate':dt.datetime(2006,5,15)},
    { 'studid': 8 , 'studname': 'deepak thakur', 'studDOB' : dt.datetime(2001,8,3),'studAddDate':dt.datetime(2005,6,11)},
    { 'studid': 9 , 'studname': 'praksh tivari', 'studDOB' : dt.datetime(2000,9,2),'studAddDate':dt.datetime(2006,6,21)},
    { 'studid': 10 ,'studname': 'anil kapur', 'studDOB' : dt.datetime(2001,10,1),'studAddDate':dt.datetime(2005,6,6)},
]


def info(req):
    response = render(req,'pathshala/index.html',{'studlist':studlist})
    return response

def about(req):
    return render(req,'pathshala/about.html')

from django.views import View
from django.shortcuts import redirect

class delete(View):
    def get(self,req,id):
        for stud in studlist:
            if stud['studid'] == id :
                return render(req,'pathshala/confirm.html',{'stud':stud})

    def post(self,req,id):
        for stud in studlist:
            if stud['studid']== id:
                studlist.remove(stud)
                return redirect('/index')

class update(View):
    def get(self,req,id):
        for stud in studlist:
            if stud['studid'] == id:
                return render(req,'pathshala/form.html',{'stud':stud})
    
    def post(self,req,id):
        for stud in studlist:
            if stud['studid'] == id:
                stud['studname'] = req.POST['studname']
                Bdate = req.POST['studDOB']
                stud['studDOB']=dt.datetime.strptime(Bdate,'%d-%m-%Y')
                Adate =req.POST['studAddDate']
                stud['studAddDate'] = dt.datetime.strptime(Adate,'%d-%m-%Y')
                return redirect('/index')

class add(View):
    def get(self,req):
        stud = {}
        return render(req,'pathshala/form.html',{'stud':stud})

    def post(self,req):
        stud = {}
        stud['studid'] = req.POST['studid']
        stud['studname'] = req.POST['studname']
        Bdate = req.POST['studDOB']
        stud['studDOB']=dt.datetime.strptime(Bdate,'%d-%m-%Y')
        Adate =req.POST['studAddDate']
        stud['studAddDate'] = dt.datetime.strptime(Adate,'%d-%m-%Y')
        studlist.append(stud)
        return redirect('/index')

        
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from Hospital.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def Index(request):
    return redirect('logout')

def Login(request):    
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user= authenticate(username=u,password=p)
        if user.is_staff:
            login(request,user)
            return render(request,'index.html')
        else:
            return redirect('login')     
    return render(request,'login.html')

def Logout_admin(request):
    logout(request)
    return redirect('login')
    
def View_Doctor(request):
    if not request.user.is_staff :
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'veiw_doctor.html',d)


def Add_Doctor(request):    
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        s=request.POST['special']
        Doctor.objects.create(name=n,mobile=c,special=s)
         
    return render(request,'add_doctor.html')

def View_Patient(request):
    if not request.user.is_staff :
        return redirect('login')
    pat=Patient.objects.all()
    p={'pat':pat}
    return render(request,'view_patient.html',p)

def Add_Patient(request):
        
    if request.method=='POST':
        n=request.POST['name']
        g=request.POST['gender']
        m=request.POST['mobile']
        a=request.POST['address']
        Patient.objects.create(name=n,gender=g,mobile=m,address=a) 
    return render(request,'add_patient.html')


def View_Appointment(request):
    if not request.user.is_staff :
        return redirect('login')
    apt=Appoinment.objects.all()
    a={'apt':apt}
    return render(request,'view_Appointment.html',a)

def Add_Appointment(request):    
    if request.method=='POST':
        i=request.POST['id']
        doc=request.POST['doctor']
        p=request.POST['patient']
        d=request.POST['date']
        t=request.POST['time']
        Appoinment.objects.create(id=i,doctor=doc,patient=p,date=d,time=t) 
    return render(request,'add_appointment.html')

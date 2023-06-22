
from django.shortcuts import render
from . models import *
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request,'index.html')
def signup(request):
    '''if request.method=='POST':
      signup = Signup()
      name = request.POST.get('name')
      age = request.POST.get('age')
      gender = request.POST.get('gender')
      number = request.POST.get('number')
      email = request.POST.get('email')
      password = request.POST.get('password')
      signup.name=name
      signup.age=age
      signup.gender=gender
      signup.number=number
      signup.email=email
      signup.password=password
      signup.save()'''
    '''if request.method=='POST':
        login = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        login.email=email
        login.password=password
        login.save()
        return HttpResponse('<h1>Thanks</h1>')'''
    if request.method == 'POST':
        signup=Signup()
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        number = request.POST.get('number')
        #email = request.POST.get('email')
        password = request.POST.get('password')
        signup.name=name
        signup.age=age
        signup.gender=gender
        signup.number=number
        #signup.email=email
        signup.password=password
        signup.save()

            

      #return HttpResponse('<h1>Thanks</h1>')

      
    
    return render(request,'signup.html')
def signin(request):
    if request.method=='POST':
        login = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        login.email=email
        login.password=password
        login.save()
        return HttpResponse('<h1>Thanks</h1>')

    return render(request,'signin.html')
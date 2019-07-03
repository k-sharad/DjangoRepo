from django.shortcuts import render
from testapp.models import Employee

# Create your views here.

def home_view(request):
    return render(request,"testapp/home.html")

def emp_view(request):
 employees=Employee.objects.all()
 return render(request,"testapp/showemp.html",{'employees':employees})
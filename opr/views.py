from django.shortcuts import render
from django.http import request, HttpResponse
from .models import *

# Create your views here.

# ****************   FOR ALL() METHOD    *****************

def all_data(request):
    student_data=Student.objects.all()
    teacher_data=Teacher.objects.all()
    
    return render (request,'student.html',{"student_data":student_data, "teacher_data":teacher_data})

# *****************   FOR GET() METHOD  ******************

def single_data(request):
    student_data=Student.objects.get(roll_number = 4)
    teacher_data=Teacher.objects.get(first_name = "siya")
    

    return render (request,'single.html',{"student" : student_data, "teacher" : teacher_data})


# ******************   FOR FILTER() METHOD  ****************


def common_data(request):
    teacher_data=Teacher.objects.filter(subject = "oops")
    student_data=Student.objects.filter(age = 20)
    
   # print(teacher_data)

    return render (request,'filter.html',{"teachers" : teacher_data, "students" : student_data})


def filter_data(request):
    first_same=Student.objects.filter(first_name = "samita")
    last_same=Student.objects.filter(last_name = "yadav")
    #first_last=Student.objects.filter(first_name = "samita",last_name = "yadav")
    first_last=Student.objects.filter(first_name = "pragati" , last_name = "dhage")

    age_same=Student.objects.filter(age = 20)
    
    return render (request,'filter_method.html',{"first_same" : first_same, "last_same" : last_same, "first_last" : first_last, "age_same" : age_same})


# ********************************* FOR ADD() METHOD ***************************

def add_data(request):
    Teacher.objects.create(first_name = 'neha', last_name = 'kunjir', subject = 'science', age = 16)
    Student.objects.create(first_name = 'karan', last_name = 'koli', roll_number = 75, age = 23)
    return HttpResponse("data added")




def signin(request):
    return HttpResponse("this is signin page")

def login(request):
    return HttpResponse("this is login page") 


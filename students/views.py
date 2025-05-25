from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {"name": "John", "age": 20},
        {"name": "Jane", "age": 22},
        {"name": "Mike", "age": 21},
    ]
    return HttpResponse(students)
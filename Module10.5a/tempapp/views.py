
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def temp(request):
    d = { 
        'name': 'rokon',
        'id': '38',
        'list': ['Hello','World'],
        'birthday':datetime.datetime.now(),
        'val':10,
        'l1':[1,2,3],
        'l2':[9,8,7],
        'c':"Hello world!",
        'ci':[ "Hello", "World!","Happy"," Journey"],
        'di' : [
         {'name': 'Josh', 'age': 19},
         {'name': 'Dave', 'age': 22},
         ]   ,
         'tw':"Hello World Happy Journey"  ,

        
    }
    return render(request, "temp.html", d)

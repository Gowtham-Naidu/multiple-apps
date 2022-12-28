from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse("<h1>this is  string1 in app1</h1>")

def string2(request):
    return HttpResponse("<h1>this is string2 in app1</h1>")
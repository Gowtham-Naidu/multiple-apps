from django.shortcuts import render

# Create your views here.
def onehtml(request):
    return render(request,'one.html')

def twohtml(request):
    return render(request,'two.html')
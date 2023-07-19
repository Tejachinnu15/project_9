from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'hello.html')
def how(request):
    return render(request,'how.html')
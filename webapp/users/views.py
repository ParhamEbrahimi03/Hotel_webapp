from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("<h1>This is home</h1>")
    return render(request, 'users/home.html')

def service(request):
    return render(request, 'users/service.html')

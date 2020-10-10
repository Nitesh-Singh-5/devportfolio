from django.shortcuts import render

# Create your views here.

def services(request):
    return render(request,'serv/services.html',context= {'services':'active'})
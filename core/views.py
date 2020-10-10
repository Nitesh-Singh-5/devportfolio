from django.shortcuts import render
from .forms import studentRegistration
from .models import User
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request,'core/home.html',{'home':'active'})

def showdata(request):
    if request.method == 'POST':
        fm= studentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            msg= fm.cleaned_data['message']
            reg=User(name=nm,email=em,message=msg)
            reg.save()
            return HttpResponse('Thank you! for your message ')
            fm=studentRegistration()
            
    else:   
        fm= studentRegistration()
    return render(request,'core/contact.html',{'form':fm,'contact':'active'})



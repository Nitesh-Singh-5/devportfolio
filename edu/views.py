from django.shortcuts import render

# Create your views here.
def skill(request):
    return render(request,'edu/skill.html',context= {'skill':'active'})
from django.shortcuts import render
from .models import internshipPost

def home(request):
    internships = internshipPost.objects.all()
    return render(request,'InternsOnboardMain/home.html',{'internships':internships})

def about(request):
    return render(request,'InternsOnboardMain/about.html')

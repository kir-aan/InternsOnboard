from django.shortcuts import render

def home(request):
    return render(request,'InternsOnboardMain/home.html')

def about(request):
    return render(request,'InternsOnboardMain/about.html')

from django.shortcuts import render
from .models import internshipPost
from coordinatorPortal.models import finalApplicants

def home(request):
    internships = internshipPost.objects.all()
    finalApplicant = finalApplicants.objects.all()
    return render(request,'InternsOnboardMain/home.html',{'internships':internships,'finalApplicant':finalApplicant})

def about(request):
    return render(request,'InternsOnboardMain/about.html')

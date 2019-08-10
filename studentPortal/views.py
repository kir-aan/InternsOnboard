from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import studentInternship
from .forms import studentInternshipForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from InternsOnboardMain.models import internshipPost

@login_required
def apply(request):
    if "applybtn" in request.POST:
        # currentStudentName = request.user
        # c = request.POST['c_name']
        # currentCompany=internshipPost.objects.get(company_name=c)
        # studentinternship = studentInternship(
        #     studentName=currentStudentName,
        #     applied=True,
        #     companyName= currentCompany
        # )
        messages.success(request, 'Applied!')
    elif "rejectbtn" in request.POST:
        messages.warning(request, 'Rejected')
    return redirect('InternsOnboard-Home')

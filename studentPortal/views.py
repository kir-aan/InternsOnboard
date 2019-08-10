from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import studentInternship
from .forms import studentInternshipForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from InternsOnboardMain.models import internshipPost
from django.db.models import Q

@login_required
def apply(request):
    if "applybtn" in request.POST:
        currentStudentName = request.user
        c = request.POST['c_name']
        currentCompany=internshipPost.objects.get(company_name=c)
        try:
            p=studentInternship.objects.get(companyName__exact=currentCompany,studentName__exact=currentStudentName)
            if p:
                if p.applied==True:
                    messages.warning(request, 'Already applied!')
                elif p.applied==False:
                    p.applied=True
        except studentInternship.DoesNotExist :
            studentinternship = studentInternship(
                studentName=currentStudentName,
                applied=True,
                companyName= currentCompany
            )
            messages.success(request, 'Applied!')
    elif "rejectbtn" in request.POST:
        messages.warning(request, 'Rejected')
    return redirect('InternsOnboard-Home')

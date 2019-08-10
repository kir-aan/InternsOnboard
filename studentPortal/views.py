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
        #check if currentStudentName name is linked with currentCompany
            ## if applied ==TRUE
                ##true --> warning --> already submitted
                ##false --> current row, applied=TRUE
        ## else --> create db entry
        try:
            queryset = studentInternship.objects.filter(studentName=currentStudentName)
            test = 0
            for q in queryset:
                if q.companyName.company_name == c:
                    if q.applied==True:
                        messages.warning(request,'Already applied!')
                    else:
                        q.applied=True
                        q.save()
                        messages.success(request,"Applied!")
                    test=1
            if test==0:
                studentinternship = studentInternship(studentName=currentStudentName,applied=True,companyName= currentCompany)
                studentinternship.save()
                messages.success(request,"Applied!")
        except Exception as e:
            messages.warning(request,"SOMETHING WENT WRONG"+"\nError " + str(e))
    else:
        currentStudentName = request.user
        c = request.POST['c_name']
        currentCompany=internshipPost.objects.get(company_name=c)
        #check if currentStudentName name is linked with currentCompany
            ## fetch currentCompany linked with currentCompany and set applied=FALSE
        # add currentStudentName linked with currentCompany as rejected.
        try:
            queryset = studentInternship.objects.filter(studentName=currentStudentName)
            test = 0
            for q in queryset:
                if q.companyName.company_name == c:
                    q.applied=False
                    q.save()
                    test=1
            if test==0:
                studentinternship = studentInternship(studentName=currentStudentName,applied=False,companyName= currentCompany)
                studentinternship.save()

            messages.warning(request,'Rejected!')
        except Exception as e:
            messages.warning(request,"Unexpected error: "+str(e))

    return redirect('InternsOnboard-Home')

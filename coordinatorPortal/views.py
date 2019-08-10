from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InternshipsUploadForm
from InternsOnboardMain.models import internshipPost
from django.contrib.auth.models import User
from studentPortal.models import studentInternship
from rest_framework.generics import ListAPIView
from .serializers import internshipSerializer
from .models import finalApplicants

class internshipListAPIView(ListAPIView):
  queryset = internshipPost.objects.all()
  serializer_class = internshipSerializer


@login_required
def post(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InternshipsUploadForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            internshipForm = form.save(commit=False)
            internshipForm.owner = request.user
            internshipForm.Uploader_info = request.user
            company_name = form.cleaned_data.get('company_name')
            internshipForm.save()
            messages.success(request, 'Internship for {} Posted successfully'.format(company_name))
            return redirect('InternsOnboard-Home')
        else:
            parameters = {
              'form': form,
              'error': form.errors.as_ul()
            }
            return render(request, 'coordinatorPortal/post.html', parameters)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InternshipsUploadForm()
        return render(request, 'coordinatorPortal/post.html', {'form': form})


def applications(request):
    internApplication = studentInternship.objects.all()
    return render(request,'coordinatorPortal/applications.html',{'internApplication':internApplication})



# check if company_Name and student_Name is already in the db:
	#True-->
		# update/don't update based on accepted value currently stored.
	#False-->create a new db entry with selected button as accepted status
# accepted = True if accept button clicked, False if reject button clicked
@login_required
def accept(request):
    if "acceptbtn" in request.POST:
        currentStudentName = request.POST.get('s_name')
        currentCompanyName = request.POST.get('c_name')
        try:
            queryset = finalApplicants.objects.filter(student_Name=currentStudentName)
            check = 0
            for q in queryset:
                if q.company_Name == currentCompanyName:
                    if q.accepted:
                        messages.warning(request,"Already accepted")
                    else:
                        q.accepted=True
                        q.save()
                        messages.success(request,"Accepted!")
                    check = 1
            if(check==0):
                finalApplicants.objects.create(
                    student_Name = currentStudentName,
                    company_Name = currentCompanyName,
                    accepted = True
                )
                messages.success(request,"Accepted!")
        except Exception as e:
            messages.warning(request,"Unexpected error: "+str(e))
    else:
        currentStudentName = request.POST.get('s_name')
        currentCompanyName = request.POST.get('c_name')
        try:
            queryset = finalApplicants.objects.filter(student_Name=currentStudentName)
            check = 0
            for q in queryset:
                if q.company_Name == currentCompanyName:
                    if q.accepted:
                        q.accepted=False
                        q.save()
                        messages.warning(request,"Rejected!")
                    else:
                        messages.warning(request,"Already Rejected!")
                    check = 1
            if(check==0):
                finalApplicants.objects.create(
                    student_Name = currentStudentName,
                    company_Name = currentCompanyName,
                    accepted = False
                )
                messages.success(request,"Rejected!")
        except Exception as e:
            messages.warning("Unexpected error: "+str(e))
    
    return redirect('internship-applications')

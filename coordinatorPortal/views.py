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


@login_required
def accept(request):
    currentStudentName = request.POST.get('s_name')
    currentCompanyName = request.POST.get('c_name')
    # currentCompany=studentInternship.objects.get(companyName=currentCompanyName)
    # currentStudent=studentInternship.objects.get(studentName=currentStudentName)
    finalApplicants.objects.create(
        accepted=True,
        company_Name=currentCompanyName,
        student_Name=currentStudentName
    )
    messages.success(request, 'Accepted!')
    return redirect('internship-applications')
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import studentInternship
from .forms import studentInternshipForm
from django.contrib import messages
from django.contrib.auth.models import User

# def apply(request):
#     if request.GET.get('applybtn'):
#         profil = get_object_or_404(studentInternship)
#         profil.applied = True
#         profil.save(update_fields=["applied"])
#         # profil.create(applied=True)
#         return render(request, 'InternsOnboard-Home')
#     return render(request, 'InternsOnboardMain/home.html')

def apply(request):
    if studentInternship.applied:
        studentinternship = studentInternship(
            applied=True
        )
        studentinternship.save()
        messages.success(request, 'Applied!')
    else:
        messages.warning(request,'You have already applied!')
    return redirect('InternsOnboard-Home')

            
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InternshipsUploadForm
from InternsOnboardMain.models import internshipPost
from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView
from .serializers import internshipSerializer

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
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.userprofile.usertype = form.cleaned_data.get('usertype')
            user.userprofile.username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            # login(request, user) -->Auto Logins after registration.
            messages.success(request, 'Account created for {}, You may login now!'.format(user.username))
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'userRegister/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request, 'Proflie Updated!')
             return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'userRegister/profile.html',context)

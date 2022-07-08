from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UsrUpdate, ProfUpdate
from django.contrib.auth.decorators import login_required

def user_registration(request):
	if request.method == 'POST':
		reg_form = UserCreationForm(request.POST)
		if reg_form.is_valid():
			reg_form.save()
			return redirect('home_page')
	else:
		reg_form = UserCreationForm()
	return render(request, 'users/registration.html', {'reg_form': reg_form})

@login_required
def profile(request):
    if request.method == 'POST':
        usr_form = UsrUpdate(request.POST, instance=request.user)
        prof_form = ProfUpdate(request.POST, request.FILES, instance=request.user.profile)
        if usr_form.is_valid() and prof_form.is_valid():
            usr_form.save()
            prof_form.save()
    else:
        usr_form = UsrUpdate(instance=request.user)
        prof_form = ProfUpdate(instance=request.user.profile)
    return render(request, 'users/profile.html', {'usr_form':usr_form, 'prof_form': prof_form})

    
        
    

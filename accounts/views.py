from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser

def registerPage(request):
	form = CreateUser()

	if request.method == 'POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			form.save()
	context={'form':form}
	return render(request,'accounts/register.html',context)




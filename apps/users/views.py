from django.shortcuts import render, redirect
# from apps.users.forms import UserProfileForm
from apps.users.forms import RegisterForm
from django.views.generic import View
from django.contrib.auth import login, authenticate, forms, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class Register(View):
	form = RegisterForm
	def get(self, request):
		context = {'form': self.form()}
		return render(request, 'users/register.html', context)
	def post(self, request):
		form = self.form(request.POST)

		if form.is_valid():
			form.save()

			return redirect('/login')
		else:
			context = {'form': form}
			return render(request, 'users/register.html', context)

class Login(View):
	form = forms.AuthenticationForm
	def get(self, request):
		context = {'form': self.form()}
		return render(request, 'users/login.html', context)
	def post(self, request):
		form = self.form(None, request.POST)
		context = {'form': form}
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/dashboard')
			else:
				return render(request, 'users/login.html', context)
		else:
			return render(request, 'users/login.html', context)

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect('/login');

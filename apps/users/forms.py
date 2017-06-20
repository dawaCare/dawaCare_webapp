from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from models import UserProfile

# class UserProfileForm(forms.ModelForm):

# 	class Meta:
# 		model = UserProfile
# 		fields = ('name',)


class RegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)

		if commit:
			user.save()
			return user

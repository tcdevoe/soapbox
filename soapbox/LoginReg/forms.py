from django.forms import ModelForm
from LoginReg.models import User

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['Email','Password']

class RegistrationForm(ModelForm):
	class Meta:
		model = User
		fields = ['FirstName', 'LastName', 'Email', 'Password']

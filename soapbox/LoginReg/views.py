from django.http import HttpResponse
from django.shortcuts import render
from LoginReg import forms

# Create your views here.


def index(request):
	if request.method == 'POST' ## If the form has been submitted, do this
		form = LoginForm(request.Post)
		# if form.isvalid():   ## Implement this function to check for valid for submission
		return HttpResponse("Submitted a Form!")
	else:
		form = LoginForm()

	return render(request, 'index.html', {
		'form': form,
	})

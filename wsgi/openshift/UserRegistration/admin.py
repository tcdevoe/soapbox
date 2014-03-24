from UserRegistration.models import SBUser
from django.contrib import admin

class SBUserAdmin(admin.ModelAdmin) :
	fields = ['email', 'username', 'password']

admin.site.register(SBUser)
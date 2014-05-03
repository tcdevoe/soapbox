import datetime
from django.utils import timezone
from django.db import models



# Create your models here.

#
# This represents a Basic User. Will expand upon as necesssary
#
class User(models.Model):
        FirstName = models.CharField(max_length=50)
        LastName = models.CharField(max_length=50)
        Email = models.EmailField()
        # Make sure to use Password Input form
        Password = models.CharField(max_length=100)
	RegDate = models.DateField()

	def __unicode__(self):
		return self.FirstName+" "+self.LastName+","+self.Email

	def registeredToday(self):
		return self.RegDate >= timezone.now() - datetime.timedelta(days=1)
	

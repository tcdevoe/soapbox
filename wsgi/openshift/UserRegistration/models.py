from django.db import models

# This is a temporary implementation of what the User
# Registration tables could look like


# Not sure if we should do field validation on the
# front end or the back end

class SBLocation(models.Model) :
    country = models.CharField(max_length=100)	# TODO : Change this to list of all valid countries
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class SBUser(models.Model) :
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18) # TODO : Need to change to make sure plaintext password is never stored
    email = models.EmailField() # Max length of an email address


def __unicode__(self):
    return self.username

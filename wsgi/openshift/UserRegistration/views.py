from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from models import SBUser

def index(request):
    alph_users = SBUser.objects.all().order_by('username')

    # t = loader.get_template('UserRegistration/index.html')
    # c = Context({
    #     'alph_users': alph_users,
    # })
    # This is equivalent to the shortcut Django provides below :

    return render_to_response('UserRegistration/index.html', {'alph_users': alph_users})
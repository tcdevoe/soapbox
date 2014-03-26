from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a test of the Views.")
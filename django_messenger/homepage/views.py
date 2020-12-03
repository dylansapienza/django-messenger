from django.http import HttpResponse

def home(request): 
    return HttpResponse("Github is forever and poop")
from django.shortcuts import render

# Homepage Views!


def home(request):
    return render(request, 'homepage/home.html')

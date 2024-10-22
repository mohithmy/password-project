from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def home(Request):
    return render(Request, 'generator/home.html')

def password(request):
    Characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        Characters.extend(list('0123456789'))
    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()_,./'))
    length = int(request.GET.get('length',8))
    thepassword=''

    for x in range(length):
        thepassword += random.choice(Characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
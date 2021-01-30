from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # to return a string, you need to use http.response
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvqxyz')
    # check to see if user wants uppercase
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # check if user wants special characters
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    # check if they want numbers
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    # if nothing is entered, use default length as 12
    length = int(request.GET.get('length',12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
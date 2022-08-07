from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'authentication/index.html')

def signUp(request):
    return render(request,'authentication/signUp.html')

def signIn(request):
    return render(request,'authentication/signIn.html')

def signOut(request):
    return render(request,'authentication/signOut.html')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return HttpResponse("This is a student profile")

def home(request):
    return HttpResponse("You are in Home page")
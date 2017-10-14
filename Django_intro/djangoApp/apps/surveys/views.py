from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response = "placeholder to later display all surveys"
    return HttpResponse(response)

def all_surveys(request):

    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new_surveys(request):

    response = "placeholder for users to add a new survey"
    return HttpResponse(response)

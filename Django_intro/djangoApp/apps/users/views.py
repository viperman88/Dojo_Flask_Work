from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response = "placeholder to later display all users"
    return HttpResponse(response)

def register(request):

    response =  'placeholder for users to create a new user record'
    return HttpResponse(response)

def login(request):

    response = 'placeholder for users to login'
    return HttpResponse(response)

def new_user(request):

    response = "placeholder for users to add a new survey"
    return HttpResponse(response)

def users(request):

    response = 'placeholder to later display all the list of users'
    return HttpResponse(response)

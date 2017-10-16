from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Book authors app working!"
    return HttpResponse(response)

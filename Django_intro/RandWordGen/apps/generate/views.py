from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

    try:
        request.session['attempts']
    except KeyError:
        request.session['attempts'] = 0

    #context = get_random_string(length=32)
    #context = {
    #    "randWord": get_random_string(length=14)
    #}
    return render(request,'generate/index.html')

def generate(request):
    request.session['attempts'] += 1
    request.session['randWord'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    del request.session['attempts']
    del request.session['randWord']
    return redirect('/')

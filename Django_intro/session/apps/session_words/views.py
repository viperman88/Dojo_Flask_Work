from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):

    return render(request, 'session_words/index.html')

def process(request):

    new_word = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "largeFont":
            new_word[key] = value
        if key == "largeFont":
            new_word['large'] = "large"
        else:
            new_word['large'] = ""
    new_word['created_at'] = datetime.now().strftime("%-I:%M %p, %B %d, %Y")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.append(new_word)
    request.session['words'] = temp_list

    #for key, val in request.session.__dict__.iteritems():
        #print key, val
    #print "past craeted at", new_word

    return redirect('/')

def reset(request):

    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

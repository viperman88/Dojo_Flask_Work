from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    try:
        request.session['attempts']
    except KeyError:
        request.session['attempts'] = 0
    return render(request,'info/index.html')

def process(request):
    request.session['attempts'] += 1
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    return render(request, 'info/results.html')

def reset(request):
    del request.session['name']
    del request.session['location']
    del request.session['language']
    del request.session['comments']
    return redirect('/')

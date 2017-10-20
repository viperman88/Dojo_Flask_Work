from __future__ import unicode_literals
from django.contrib import messages
import bcrypt
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, 'logReg/index.html')

def process(request):

    errors = User.objects.user_reg_validation(request.POST)
    print 'error len', len(errors)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    else:
        new_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print new_hash
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=new_hash)
        new_user.save()
        request.session['id'] = new_user.id
        return redirect('/success')

    return render(request, 'logReg/index.html')

def success(request):

    return render(request, 'logReg/success.html')

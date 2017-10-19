from __future__ import unicode_literals
from .models import Course
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'classes/index.html',context)

def add_course(request):

    errors = Course.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
    return redirect('/')

    #errors = Course.objects.validate(request.POST)
    #if len(errors):
        #for field, message in errors.iteritems():
            #error(request, message, extra_tags=field)
    #return redirect('/courses')

    #Course.objects.create(
        #name=request.POST['name'],
        #description=request.POST['description']
    #)
    #return redirect('/courses')

def remove(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'classes/remove.html',context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/courses')

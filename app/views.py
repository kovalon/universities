from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

from app.models import University


def index(request):
    return render(request, 'app/index.html')


def universities(request):
    universities = University.objects.order_by('name')
    context = {
        'universities': universities,
    }
    return render(request, 'app/universities.html', context)


def create_university(request):
    university = University(name=request.POST['name'],
                            address=request.POST['address'],
                            subjects=request.POST['subjects'])
    university.save()
    return redirect('/app/universities/')


def university(request, university_id):
    university = University.objects.get(pk=university_id)
    context = {
        'university': university,
    }
    return render(request, 'app/university.html', context)


def delete_university(request, university_id):
    obj = University.objects.get(id=university_id)
    obj.delete()
    return redirect('/app/universities/')

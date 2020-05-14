import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from faker import Faker

from teachers.models import Teacher
from teachers.forms import TeacherCreateForm

fake = Faker("uk_UA")
stups = ['professor', 'docent', 'assistant']


def make_fake_teacher() -> Teacher:
    return Teacher(first_name=fake.first_name(), last_name=fake.last_name(), stupen=random.choice(stups))


def generate_teachers(request):
    teach = []
    count = request.GET.get('count', 20)
    response = "Teachers have been generated"
    if count.isdigit() and 0 < int(count) <= 120:
        for _ in range(int(count) + 1):
            teach.append(make_fake_teacher())
        Teacher.objects.bulk_create(teach)
    else:
        response = "Invalid parameter"
    return HttpResponse(response)


def show_filtered_teachers(request):
    response = ""
    teach = Teacher.objects.all()
    fn = request.GET.get('first_name', None)
    ln = request.GET.get('last_name', None)
    if fn is not None:
        teach = Teacher.objects.filter(first_name=fn)
    if ln is not None:
        teach = Teacher.objects.filter(last_name=ln)
    teach = list(teach)
    for obj in teach:
        response += f'{obj.full_name}</br>'
    return HttpResponse(response)


def index(request):
    return render(request, 'index.html')


def create_teacher(request):
    form = TeacherCreateForm(request.GET)

    context = {'create_form': form}

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'create-teacher.html', context=context)

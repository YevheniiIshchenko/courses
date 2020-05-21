import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from faker import Faker

from teachers.forms import TeacherCreateForm
from teachers.models import Logger, Teacher


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
    return render(request, 'show-teachers.html', context={'teachers': teach})


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def create_teacher(request):
    if request.method == "POST":
        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:show_filtered'))

    elif request.method == "GET":
        form = TeacherCreateForm()

    return render(request, 'create-student.html', context={'form': form})


@csrf_exempt
def edit_teacher(request, pk):

    teach = get_object_or_404(Teacher, id=pk)

    if request.method == "POST":
        form = TeacherCreateForm(request.POST, instance=teach)

        if 'delete' in request.POST:
            teach.delete()
            return HttpResponseRedirect(reverse('teachers:show_filtered'))

        elif 'submit' in request.POST:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('teachers:show_filtered'))

    elif request.method == "GET":
        form = TeacherCreateForm(instance=teach)

    return render(request, 'edit-teacher.html', context={'form': form})


def show_logs(request):
    response = ""
    logs = Logger.objects.all().iterator()
    for log in logs:
        response += log.info()+'<br>'
    return HttpResponse(response)

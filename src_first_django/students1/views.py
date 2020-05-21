import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from faker import Faker

from students1.forms import StudentCreateForm
from students1.models import Student


fake = Faker("uk_UA")


def make_fake_student() -> Student:
    return Student.objects.create(first_name=fake.first_name(),
                                  last_name=fake.last_name(),
                                  age=random.randint(16, 70),
                                  phone=fake.phone_number())


def generate_student(request):
    st = make_fake_student()
    response = st.show_student() + '<br/>'
    return HttpResponse(response)


def generate_students(request):
    count = request.GET.get('count', 100)
    response = ""
    if not str(count).isdigit():
        response = "Invalid parameter"
    elif 0 <= int(count) <= 100:
        count = int(count)
        for _ in range(count):
            st = make_fake_student()
            response += st.show_student() + '<br/>'
    else:
        response = "Invalid parameter"
    return HttpResponse(response)


@csrf_exempt
def create_student(request):
    if request.method == "POST":
        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:show'))

    elif request.method == "GET":
        form = StudentCreateForm()

    return render(request, 'create-student.html', context={'form': form})


@csrf_exempt
def edit_student(request, pk):

    stud = get_object_or_404(Student, id=pk)

    if request.method == "POST":
        form = StudentCreateForm(request.POST, instance=stud)

        if 'delete' in request.POST:
            stud.delete()
            return HttpResponseRedirect(reverse('students:show'))

        elif 'submit' in request.POST:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('students:show'))

    elif request.method == "GET":
        form = StudentCreateForm(instance=stud)

    context = {"form": form, "id": pk, "method": str(request.method), "isvalid": form.is_valid()}
    return render(request, 'edit-student.html', context=context)


def show_students(request):
    st = Student.objects.all()
    return render(request, 'show-students.html', context={'students': st})

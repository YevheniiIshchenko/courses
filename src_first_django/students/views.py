from django.shortcuts import render

# Create your views here.
from students.models import Student
from faker import Faker

import random
import string

fake = Faker("uk_UA")


def generate_student(request):
    st = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), age=random.randint(5, 120))
    response = show_student(st) + '<br/>'
    return HttpResponse(response)


def generate_students(request):
    count = request.GET.get('count', 100)
    response = ""
    if not count.isdigit():
        response = "Invalid parameter"
    elif 0 <= int(count) <= 100:
        count = int(count)
        for _ in range(count + 1):
            st = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                        age=random.randint(5, 120))
            response += show_student(st) + '<br/>'
    else:
        response = "Invalid parameter"
    return HttpResponse(response)

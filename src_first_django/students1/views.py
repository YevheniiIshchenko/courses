import random

from django.http import HttpResponse
from django.shortcuts import render  # noqa

from faker import Faker

from students1.models import Student


fake = Faker("uk_UA")


def generate_student(request):
    st = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), age=random.randint(5, 120))
    response = st.show_student() + '<br/>'
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
            response += st.show_student() + '<br/>'
    else:
        response = "Invalid parameter"
    return HttpResponse(response)

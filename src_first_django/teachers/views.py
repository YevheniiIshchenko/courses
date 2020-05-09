from django.http import HttpResponse
from django.shortcuts import render  # noqa

from teachers.models import Teacher


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

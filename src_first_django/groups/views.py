from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from groups.forms import GroupCreateForm
from groups.models import Group


def create_group(request):
    form = GroupCreateForm(request.GET)
    context = {"create_form": form}

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, "create_group.html", context=context)


def show_groups(request):
    response = ""
    gr = list(Group.objects.all())
    for group in gr:
        response += f'{group.code_of_group}</br>'
    return HttpResponse(response)

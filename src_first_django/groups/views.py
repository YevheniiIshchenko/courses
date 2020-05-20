from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


from groups.forms import GroupCreateForm
from groups.models import Group


@csrf_exempt
def create_group(request):
    if request.method == "POST":
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:show'))

    elif request.method == "GET":
        form = GroupCreateForm()

    return render(request, 'create-student.html', context={'form': form})


def show_groups(request):
    response = ""
    gr = list(Group.objects.all())
    for group in gr:
        response += f'{group.code_of_group}</br>'
    return render(request, 'show-groups.html', context={'groups': gr})


@csrf_exempt
def edit_group(request, pk):

    gr = get_object_or_404(Group, id=pk)

    if request.method == "POST":
        form = GroupCreateForm(request.POST, instance=gr)

        if 'delete' in request.POST:
            gr.delete()
            return HttpResponseRedirect(reverse('groups:show'))

        elif 'submit' in request.POST:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('groups:show'))

    elif request.method == "GET":
        form = GroupCreateForm(instance=gr)

    return render(request, 'edit-group.html', context={'form': form})

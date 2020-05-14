from django import forms

from groups.models import Group


class GroupCreateForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ("facult", "spec", "year", "number_of_students")

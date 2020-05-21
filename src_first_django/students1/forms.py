from django import forms
from django.core.exceptions import ValidationError

from students1.models import Student


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ("first_name", "last_name", "age", "phone")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        for char in phone:
            if not char.isdigit():
                raise ValidationError("In field 'phone' have to be digits only")
        return phone

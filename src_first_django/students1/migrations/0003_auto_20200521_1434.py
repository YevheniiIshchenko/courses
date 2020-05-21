# Generated by Django 2.2.12 on 2020-05-21 14:34

from django.db import migrations

from students1.models import Student


def forwards(apps, schema):
    for st in Student.objects.all().iterator():
        st.first_name = str(st.first_name).capitalize()
        st.last_name = str(st.last_name).capitalize()
        st.save(update_fields=['first_name', 'last_name'])


class Migration(migrations.Migration):

    dependencies = [
        ('students1', '0002_student_phone'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]

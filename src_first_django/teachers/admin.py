from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('stupen', 'first_name', 'last_name')


admin.site.register(Teacher, TeacherAdmin)

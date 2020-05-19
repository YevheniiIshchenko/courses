from django.contrib import admin

from students1.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')


admin.site.register(Student, StudentAdmin)

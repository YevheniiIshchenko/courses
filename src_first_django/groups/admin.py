from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('facult', 'spec', 'year', 'number_of_students')


admin.site.register(Group, GroupAdmin)

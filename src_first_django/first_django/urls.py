from django.contrib import admin
from django.urls import path


from students1 import views as students_views

from teachers import views as teachers_views

from groups import views as groups_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('generate_student', students_views.generate_student),
    path('generate_students', students_views.generate_students),

    path('show_filtered_teachers', teachers_views.show_filtered_teachers),
    path('generate_teachers', teachers_views.generate_teachers),
    path('', teachers_views.index),
    path('create-teacher', teachers_views.create_teacher),

    path('create-group', groups_views.create_group),
    path('show_groups', groups_views.show_groups),
]

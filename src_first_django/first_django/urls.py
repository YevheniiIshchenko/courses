from django.contrib import admin
from django.urls import path


from students1 import views as students_views

from teachers import views as teachers_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('generate_student', students_views.generate_student),
    path('generate_students', students_views.generate_students),
    path('show_filtered_teachers', teachers_views.show_filtered_teachers)
]

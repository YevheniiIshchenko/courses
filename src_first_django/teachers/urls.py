from django.urls import path

from teachers import views

app_name = "teachers"

urlpatterns = [
    path('show_filtered/', views.show_filtered_teachers, name='show_filtered'),
    path('generate/', views.generate_teachers, name='generate'),
    path('create/', views.create_teacher, name='create'),
    path('edit/<int:pk>', views.edit_teacher, name='edit'),
]

from django.urls import path

from students1 import views

app_name = "students"

urlpatterns = [
    path('generate_student/', views.generate_student, name='generate1'),
    path('generate_students/', views.generate_students, name='generate_many'),
    path('show/', views.show_students, name='show'),
    path('create/', views.create_student, name='create'),
    path('edit/<int:pk>/', views.edit_student, name='edit'),
]

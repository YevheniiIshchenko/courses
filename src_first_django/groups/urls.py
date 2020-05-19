from django.urls import path

from groups import views

app_name = "groups"

urlpatterns = [
    path('show/', views.show_groups, name='show'),
    path('create/', views.create_group, name='create'),
    path('edit/<int:pk>', views.edit_group, name='edit'),
]

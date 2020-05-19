from django.contrib import admin
from django.urls import include
from django.urls import path


from teachers import views as teachers_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),
    path('students/', include('students1.urls')),

    path('', teachers_views.index, name='index'),
]

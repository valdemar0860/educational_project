"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import show_all_students, create_student, create_student_by_form

urlpatterns = [
    path('admin/', admin.site.urls),
    #    путь страницы   функция которая
    #        |           отновится к этому пути      алиас пути нужен будет для тестов, темпелейтов, редиректов, вообще хорошая практика всегда его писать
    #        |               |                          |
    path('students/', show_all_students,               name='students_list'),
    path('students/create', create_student, name='students_create'),
    path('students/form/create', create_student_by_form, name='students_form_create'),
]

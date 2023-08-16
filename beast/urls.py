"""
URL configuration for beast project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import * 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task'),
    path('create/', create_task, name='create_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('line-strike/<int:id>',linestrike,name='line-strike'),
    path('task_list/',task_list,name='task_list'),
    
]

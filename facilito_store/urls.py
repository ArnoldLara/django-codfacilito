
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
        #Se registra la funcion de views, esta funcion requiere 3 parametros
        #String de la url, la funcion a asociar y un nombre
    path('',views.index, name='index'),
    path('usuarios/login', views.login,name='login'),
]

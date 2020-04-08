
from django.contrib import admin
from django.urls import path
from . import views

#Se importa la clase que se va a usar
from products.views import ProductListView

urlpatterns = [

    path('admin/', admin.site.urls),

    #Se registra la clase ProductoListView de la siguiente manera
    path('',ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view,name='login'),
    path('usuarios/logout', views.logout_view,name='logout'),
    path('usuarios/registro', views.registro,name='registro'),

]

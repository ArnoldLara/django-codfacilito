from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product


#Se implementa una vista basada en clase que permite tener mayor organización
#Ademas de que se pueden usar varias funcionalidades de Django
class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    #Se modifica este metodo para retornar la informacion que necesita el template
    def get_context_data(self, **kwargs):
        #Se crea el contexto de la clase padre
        context = super().get_context_data(**kwargs)
        #Se modifica el contexto para incluir la informacion que va a imprimir
        #el template
        context['message'] = 'Listado de Productos'

        return context


class ProductDetailView(DetailView): #id ->llave primaria
    #Con el atributo model se le especifica el modelo con el que vamos a trabajar
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        #Se crea el contexto de la clase padre
        context = super().get_context_data(**kwargs)

        print(context)

        return context

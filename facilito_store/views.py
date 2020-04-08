from django.shortcuts import render
#Se importa la funcion redirect para redirigir la sesion del usuario a un template
from django.shortcuts import redirect

from django.http import HttpResponse
#Libreria que nos sirve para autenticar usuarios en nuestro sitio web
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import messages

from .forms import RegisterForm

from django.contrib.auth.models import User

#Funcion que recibira la peticion y retornara una respuesta http

from products.models import Product

def index(request):

    #Con el metodo objects.all() se obtiene toda la tabla de productos
    products = Product.objects.all()

    return render(request,'index.html',{
        #Contexto
        #Se puede pasar valores de la vista al template, para generar paginas
        #web dinamicas
        'message':'Listado de productos',
        'title':'Productos',
        #Listado de productos, es una lista que contiene diccionarios por cada producto
        'products':products,
    })
    #return HttpResponse('Hola, el texto ha cambiado!')

#Se tuvo que renombrar la funcion porque se importo una del mismo nombre de DJango
def login_view(request):
    #Indica que tipo de request que se hizo y se imprime en consola
    print(request.method)

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        #Los atributos que devuelve el metodo POST los devuelve en un diccionario
        #Asi que se pueden consultar con el metodo get pasando la llave primeria
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)#Retorna none si no existe usuario
        if user:
            login(request,user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            #Redirige a la pagina de home
            return redirect('index')

        else:
            messages.success(request,'Usuario o contraseñas no validos')
            print("Usuario no autenticado")

    return render(request,'users/login.html',{

    })

def logout_view(request):
    logout(request)
    messages.success(request,'Sesion cerrada correctamente.')
    return redirect('login')

def registro(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        #Se obtienen los datos con el metodo cleaned data que actua como un diccionario
        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('index')

    return render(request,'users/register.html',{
        'form':form
    })

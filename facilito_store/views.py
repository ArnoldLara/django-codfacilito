from django.shortcuts import render
from django.http import HttpResponse


#Funcion que recibira la peticion y retornara una respuesta http
def index(request):
    #Se retorna un pagina renderizada, con la funcion render
    #REcibe 3 argumentos el request, el template y un contexto que mas tarde
    #lo explican

    return render(request,'index.html',{
        #Contexto
        #Se puede pasar valores de la vista al template, para generar paginas
        #web dinamicas
        'message':'Listado de productos',
        'title':'Productos',
        #Listado de productos, es una lista que contiene diccionarios por cada producto
        'products':[
            {'title':'Playera','precio':5,'stock':True},
            {'title':'Camisa','precio':7,'stock':True},
            {'title':'Mochila','precio':20,'stock':False},
            {'title':'Laptop','precio':200,'stock':False},
        ],
    })
    #return HttpResponse('Hola, el texto ha cambiado!')

def login(request):
    #Indica que tipo de request que se hizo y se imprime en consola
    print(request.method)
    if request.method == 'POST':
        #Los atributos que devuelve el metodo POST los devuelve en un diccionario
        #Asi que se pueden consultar con el metodo get pasando la llave primeria
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)



    return render(request,'users/login.html',{

    })

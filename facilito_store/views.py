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

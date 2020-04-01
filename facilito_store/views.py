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
        'message':'Nuevo mensaje desde la vista',
        'title':'titulo'
    })
    #return HttpResponse('Hola, el texto ha cambiado!')

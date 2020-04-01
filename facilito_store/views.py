from django.http import HttpResponse

#Funcion que recibira la peticion y retornara una respuesta http
def index(request):
    return HttpResponse('Hola, el texto ha cambiado!')

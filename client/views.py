from django.shortcuts import render

from django.http import HttpResponse

def client_list(request):
    return HttpResponse("Listado de clientes (vista temporal)")

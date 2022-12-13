from django.shortcuts import render, HttpResponse

def salam(request):
    return HttpResponse('Salam')
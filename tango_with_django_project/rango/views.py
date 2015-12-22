from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'bold font from context I am'}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("About Page:<a href='/rango/'>Home</a>")
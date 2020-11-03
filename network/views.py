from django.shortcuts import render

# Create your views here.

def ppl(request):
    return render(request, 'ppl.html')

def connection(request):
    return render(request, 'connection.html')
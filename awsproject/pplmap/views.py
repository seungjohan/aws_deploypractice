from django.shortcuts import render

# Create your views here.

def mapping(request):
    return render(request, 'mapping.html')
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mustard(request):
    return render(request, 'mustard.html')

def myac(request):
    return render(request, 'myac.html')

def write(request):
    return render(request, 'write.html')

def bootstrapprac(request):
    return render(request, 'bootstrapprac.html')

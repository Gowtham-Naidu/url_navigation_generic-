from django.shortcuts import render

# Create your views here.

def hi(request):
    return render(request,'intro.html')

def about(request):
    return render(request, 'about.html')
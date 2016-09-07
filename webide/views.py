from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    # load app
    return render(request, 'index.html')

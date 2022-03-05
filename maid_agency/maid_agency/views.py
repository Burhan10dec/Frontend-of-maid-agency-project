from django.shortcuts import render


def index(request):
    return render(request,'FDWs.html')


def add_FDWs(request):
    return render(request,'add_FDWs.html')
from django.shortcuts import render


def index(request):
    return render(request,'dashboard.html')

def FDWs(request):
    return render(request,'FDWs.html')

def myagency(request):
    return render(request,'My_agency.html')

def myagencyedit(request):
    return render(request,'Edit_My_agency.html')


def add_FDWs(request):
    return render(request,'add_FDWs.html')



def FDWs_profile(request):
    return render(request,'FDWs_profile.html')
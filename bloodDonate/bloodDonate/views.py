from django.shortcuts import render,HttpResponse

def base(request):
    return render(request,'base.html')
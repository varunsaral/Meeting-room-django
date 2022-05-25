from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting



def welcome(request):
    return render(request,"website/welcome.html",{"meetings":Meeting.objects.all()})

def about(request):
    return HttpResponse('About page')
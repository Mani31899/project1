from django.shortcuts import render 
from django.http import HttpResponse # Create your views here.
def home(request):
    return HttpResponse("Hello World..Good Morning. Hi i am Manikandan. Studing at St. Joseph's College of Engineering")

from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello This is pragnesh</h1>") #this is for static
    return  render(request,"index.html")

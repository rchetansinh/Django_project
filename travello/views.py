from django.shortcuts import render
from .models import destination
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello This is pragnesh</h1>") #this is for static
    dist1 =destination()
    dist2 =destination()
    dist3 =destination()
    dist1.price = 6000
    dist2.price = 9000
    dist3.price = 18000
    dist1.name ="Baroda"
    dist2.name ="Ahmedabad"
    dist3.name ="Banglore"
    dist1.dics ="Sansakari Nagari"
    dist2.dics ="Fun city"
    dist3.dics ="The it hub"
    dist1.img = "team_4.jpg"
    dist2.img = "Ahmedabad.jpg"
    dist3.img = "Banglore.jpg"
    dist1.offer = False
    dist2.offer = True
    dist3.offer =False
    dists=[dist1,dist2,dist3]
    return  render(request,"index.html",{'dists':dists})
    #return render(request, "index.html")
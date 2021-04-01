from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from .models import Admin, Client , Product, Order , Seller

# Create your views here.

def home(request):
    return render(request,"home.html")
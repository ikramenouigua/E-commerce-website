from dashbordClient.models import Productt
from django.shortcuts import render

# Create your views here.


def home(request):
    products = Productt.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

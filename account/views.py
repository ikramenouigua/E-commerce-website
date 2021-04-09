from django.shortcuts import render
from .forms import FormPerson
from .models import person
# Create your views here.


def register(request):
    form = FormPerson()
    if request.method == 'POST':
        form = FormPerson(request.POST)
        if form.is_valid():
            user = form.save()
            trade=request.POST.get('trade')
            if trade=='Seller':
                form2=FormSeller(request.POST)
                context={'form':form2}
              
                


    context = {'form': form}
    return render(request, 'register.html', context)
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    return render(request, 'login.html')

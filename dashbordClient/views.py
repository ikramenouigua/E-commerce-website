from django.shortcuts import render,redirect
from .models import Productt
from .forms import FormProduct

def showDashbord(request):
    return render(request,'homeSeller.html')
def ShowProduct(request):
    form=FormProduct
    products=Productt.objects.all()
    if request.method== 'POST':
        form=FormProduct(request.POST)
        if form.is_valid():
            print("printing" ,request.POST)
            form.save()
            return redirect('/')
        else:
            print("ERROR HADXI MAKHADAMX")
    context={'form':form,
             'products':products
             }
    return render(request,'product.html',context)

def deleteProduct(request, pk):
	product = Productt.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('/prod')

	context = {'item':product}
	return render(request, 'product', context)

def updateProduct(request, pk):

	product = Productt.objects.get(id=pk)
	form = FormProduct(instance=product)

	if request.method == 'POST':
		form = FormProduct(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/prod')

	context = {'form':form}
	return render(request, 'product.html', context)

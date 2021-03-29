from django.shortcuts import render



def showDashbord(request):
    return render(request,'dashbordClient.html')

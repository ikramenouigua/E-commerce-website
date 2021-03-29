from django.urls import path
from . import views


urlpatterns = [
    path('dashbordclient/',views.showDashbord,name='dashbordclient'),
]
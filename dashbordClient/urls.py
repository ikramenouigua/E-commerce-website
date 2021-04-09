from django.urls import path
from . import views


urlpatterns = [
    path('dashboardSeller/',views.showDashbord,name='dashboardSeller'),
    path('prod/',views.ShowProduct,name='prod'),
    path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),
]
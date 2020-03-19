from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addStock', views.addStock, name='addStock'),
    path('addStockData', views.addStockData, name='addStockData'),
    path('getStockInfo/<str:stock_code>', views.getStockInfo, name='getStockInfo')
]
from django.urls import path

from network_items import views


urlpatterns = [
    path('entrepreneur/create', views.EntrepreneurCreateView.as_view(), name='create-entrepreneur'),
    path('entrepreneur/list', views.EntrepreneurListView.as_view(), name='entrepreneur_list'),
    path('entrepreneur/<pk>', views.EntrepreneurView.as_view(), name='entrepreneur'),
    path('retail_network/create', views.RetailNetworkCreateView.as_view(), name='create-rn'),
    path('retail_network/list', views.RetailNetworkListView.as_view(), name='rn_list'),
    path('retail_network/<pk>', views.RetailNetworkView.as_view(), name='rn'),
    path('factory/create', views.FactoryCreateView.as_view(), name='create-factory'),
    path('factory/list', views.FactoryListView.as_view(), name='factory_list'),
    path('factory/<pk>', views.FactoryView.as_view(), name='factory'),
]
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from network_items import permissions
from network_items.models import Entrepreneur, RetailNetwork, Factory
from network_items.serializers import EntrepreneurCreateSerializer, EntrepreneurSerializer, \
    RetailNetworkCreateSerializer, RetailNetworkSerializer, FactoryCreateSerializer, FactorySerializer


class EntrepreneurCreateView(CreateAPIView):
    model = Entrepreneur
    permission_classes = [permissions.IsActiveUserPermission]
    serializer_class = EntrepreneurCreateSerializer


class EntrepreneurListView(ListAPIView):
    model = Entrepreneur
    permission_classes = [permissions.IsActiveUserPermission]
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()

    def list(self, request, *args, **kwargs):
        country = request.GET.get('country', None)
        if country:
            self.queryset = Entrepreneur.objects.filter(
                contacts_data__country=country
            )
        return super().list(request, *args, **kwargs)


class EntrepreneurView(RetrieveUpdateDestroyAPIView):
    model = Entrepreneur
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [permissions.IsActiveUserPermission]


class RetailNetworkCreateView(CreateAPIView):
    model = RetailNetwork
    permission_classes = [permissions.IsActiveUserPermission]
    serializer_class = RetailNetworkCreateSerializer


class RetailNetworkListView(ListAPIView):
    model = RetailNetwork
    permission_classes = [permissions.IsActiveUserPermission]
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()

    def list(self, request, *args, **kwargs):
        country = request.GET.get('country', None)
        if country:
            self.queryset = Entrepreneur.objects.filter(
                contacts_data__country=country
            )
        return super().list(request, *args, **kwargs)


class RetailNetworkView(RetrieveUpdateDestroyAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [permissions.IsActiveUserPermission]


class FactoryCreateView(CreateAPIView):
    model = Factory
    permission_classes = [permissions.IsActiveUserPermission]
    serializer_class = FactoryCreateSerializer


class FactoryListView(ListAPIView):
    model = Factory
    permission_classes = [permissions.IsActiveUserPermission]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()

    def list(self, request, *args, **kwargs):
        country = request.GET.get('country', None)
        if country:
            self.queryset = Entrepreneur.objects.filter(
                contacts_data__country=country
            )
        return super().list(request, *args, **kwargs)


class FactoryView(RetrieveUpdateDestroyAPIView):
    model = Factory
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [permissions.IsActiveUserPermission]

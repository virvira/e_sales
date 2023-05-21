from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from network_items.models import ContactsData, Product, Entrepreneur, RetailNetwork, Factory


class ContactsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsData
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class EntrepreneurCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        read_only = ('id', 'created_at')
        fields = '__all__'

    products = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='id'
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop('products', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        entrepreneur = Entrepreneur.objects.create(**validated_data)

        for item in self._products:
            item_obj = get_object_or_404(Product, id=item)
            if item_obj:
                entrepreneur.products.add(item_obj)

        entrepreneur.save()

        return entrepreneur


class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'debt')

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop('products', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, validated_data):
        entrepreneur = super().save()

        for item in self._products:
            item_obj = get_object_or_404(Product, id=item)
            if item_obj:
                entrepreneur.products.add(item_obj)

        entrepreneur.save()

        return entrepreneur




class RetailNetworkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        read_only = ('id', 'created_at')
        fields = '__all__'

    products = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='id'
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop('products', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        retail_network = RetailNetwork.objects.create(**validated_data)

        for item in self._products:
            item_obj = get_object_or_404(Product, id=item)
            if item_obj:
                retail_network.products.add(item_obj)

        retail_network.save()

        return retail_network


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'debt')

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop('products', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, validated_data):
        retail_network = super().save()

        for item in self._products:
            item_obj = get_object_or_404(Product, id=item)
            if item_obj:
                retail_network.products.add(item_obj)

        retail_network.save()

        return retail_network


class FactoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        read_only = ('id', 'created_at')
        fields = '__all__'

    products = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='id'
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop('products', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        factory = Factory.objects.create(**validated_data)

        for item in self._products:
            item_obj = get_object_or_404(Product, id=item)
            if item_obj:
                factory.products.add(item_obj)

        factory.save()

        return factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'debt')

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop('products', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, validated_data):
        factory = super().save()

        for item in self._products:
            item_obj = get_object_or_404(Product, id=item)
            if item_obj:
                factory.products.add(item_obj)

        factory.save()

        return factory


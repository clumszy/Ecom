'''
Serializers in Django REST Framework are responsible for converting objects
into data types understandable by javascript and front-end frameworks.
Serializers also provide deserialization, allowing parsed data to be converted
back into complex types, after first validating the incoming data.
'''

from rest_framework import serializers
from store.models import ( 
    Product,
    Customer,
    )
from django.contrib.auth.models import User

# Serializer that contains all the product fields:
class StoreProductsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    price = serializers.FloatField(required=False)
    description = serializers.CharField(required=False)
    digital = serializers.BooleanField(required=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ("id",
                  "name",
                  "category",
                  "price",
                  "description",
                  "digital",
                  "image")

        # fields = ["id",
        #           "name",
        #           "category",
        #           "price",
        #           "description",
        #           "digital",
        #           "image"]

        

# Serializer for User LogIn:
class UserLogInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)


# create internal user for super user:
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password',
                  'first_name',
                  'last_name')
        extra_kwargs = {'password':{'write_only':True}}


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    verification_token = serializers.FloatField(required=False)
    email = serializers.EmailField(required=False)
    profile_pic = serializers.ImageField(required=False)

    class Meta:
        model = Customer
        fields = ("user",
                  "name",
                  "verification_token",
                  "email",
                  "profile_pic")
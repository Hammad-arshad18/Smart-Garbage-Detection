from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Contact


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'


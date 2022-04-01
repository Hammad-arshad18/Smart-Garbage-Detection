from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from base.models import Contact
from .serializer import UserSerializer, ContactSerializer


# Views Here
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    userData = UserSerializer(users, many=True)
    return Response(userData.data)


@api_view(['GET'])
def getContacts(request):
    contacts = Contact.objects.all()
    contactData = ContactSerializer(contacts, many=True)
    return Response(contactData.data)

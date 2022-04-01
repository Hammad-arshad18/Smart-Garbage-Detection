from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from base.models import Contact,Blog
from .serializer import UserSerializer, ContactSerializer,BlogsSerialuizer
from django.http import HttpResponse


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


@api_view(['GET'])
def getBlogs(request):
    blogs=Blog.objects.all()
    if blogs is not None:
        blogSerializer=BlogsSerialuizer(blogs,many=True)
        return Response(blogSerializer.data)
    elif blogs is None:
        errorResponse=[
            'API /GET',
            'API /GET /Blogs /No Blogs Available',
        ]
        return Response(errorResponse)
    return HttpResponse('Api For Blogs')
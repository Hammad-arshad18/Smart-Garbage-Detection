from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def Index(request):
    data = {}
    if request.user.is_authenticated:

        return redirect("Homepage")
    else:
        if request.method == "POST":
            username = request.POST.get('uname')
            password = request.POST.get('upassword')
            if username == '' or password == '':
                messages.error(request, 'Username & Password Are Required')
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("Homepage")
        return render(request, 'base/index.html')


def Register(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        if username is not None and password is not None and email is not None:
            userRegister = User.objects.create_user(username=username, email=email, password=password)
            userRegister.save()
            return redirect("Homepage")

    return render(request, 'base/register.html')


def Logout(request):
    logout(request)
    return redirect("Index")


@login_required(login_url="/")
def Home(request):
    data = {}
    if request.method == "POST":
        name = request.POST.get('c_name')
        email = request.POST.get('c_email')
        comment = request.POST.get('c_comment')
        if name != "" and email != "" and comment != "":
            contact_form = Contact(name=name, email=email, comment=comment)
            contact_form.save()
        else:
            messages.error(request, "All Fields Are Required. PLease Fill All The Fields")
            data = {'response': 'All Fields Are Required. PLease Fill All The Fields'}

    return render(request, "base/home.html", data)


@login_required(login_url="/")
def livecam(request):
    return render(request, 'base/livecam.html')


@login_required(login_url="/")
def services(request):
    return render(request, 'base/services.html')


@login_required(login_url="/")
def about(request):
    return render(request, 'base/about.html')


@login_required(login_url="/")
def faq(request):
    return render(request, 'base/faq.html')


@login_required(login_url="/")
def Profile(request):
    name = request.user.username
    email = request.user.email
    data = {
        'name': name,
        'email': email
    }
    return render(request, 'base/profile.html', data)


@login_required(login_url="/")
def UpdatePersonal(request):
    userUpdate=User.objects.get(id=request.user.id)
    print(userUpdate)
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        if name != "" and email != "":
            print(name)
    return HttpResponse('404 Page Not Found')


@login_required(login_url="/")
def Dashboard(request):
    return render(request,'base/dashboard.html')
import logging

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import User

logging.basicConfig(filename="django.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def user_registration(request):
    """
    Function for registering user
    """
    try:
        if request.method == 'GET':
            return render(request, 'user/registration.html')

        if request.method == 'POST':
            obj = request.POST
            user = User.objects.create_user(first_name=obj.get('first_name'), last_name=obj.get('last_name'),
                                            username=obj.get('username'), password=obj.get('password'),
                                            email=obj.get('email'), mob_number=obj.get('mob_number'),
                                            location=obj.get('location'))

            user.save()
            return redirect("user_login")
        return render(request, 'user/registration.html')

    except Exception as e:
        print(e)
        logging.error(e)


def user_login(request):
    """
    Function for user login
    """
    try:
        if request.method == 'GET':
            return render(request, 'user/login.html')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('successfully login')
            return HttpResponse('invalid credential')
        return render(request, 'user/login.html')

    except Exception as e:
        logging.error(e)


def user_logout(request):
    """
    Function for user logout
    """
    try:
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("user_login")

    except Exception as e:
        logging.error(e)


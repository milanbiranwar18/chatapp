import json
import logging

from django.contrib.auth import authenticate
# Create your views here.
from django.http import JsonResponse

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
        obj = json.loads(request.body)
        if request.method == 'POST':
            user = User.objects.create_user(first_name=obj.get('first_name'), last_name=obj.get('last_name'),
                                            username=obj.get('username'), password=obj.get('password'),
                                            email=obj.get('email'), mob_number=obj.get('mob_number'),
                                            location=obj.get('location'))
            return JsonResponse({"Message": "User Registered",
                                 "data": {"id": user.id, "first_name": user.first_name, "last_name": user.last_name,
                                          "username": user.username, "email": user.email,
                                          "mob_number": user.mob_number, "location": user.location}}, status=201)
        return JsonResponse({"Message": "Method not allowed"}, status=400)
    except Exception as e:
        print(e)
        logging.error(e)
        return JsonResponse({"message": str(e), }, status=400)


def user_login(request):
    """
    Function for user login
    """
    try:
        obj = json.loads(request.body)
        if request.method == 'POST':
            # user = User.objects.filter(user_name=obj.get('user_name'), password = obj.get('password')).first()
            user = authenticate(username=obj.get('username'), password=obj.get('password'))
            if user is not None:
                return JsonResponse({"Message": "login successful"}, status=200)
            return JsonResponse({"Message": "Invalid Credential"}, status=403)
        return JsonResponse({"Message": "Method not allowed"}, status=400)

    except Exception as e:
        logging.error(e)
        return JsonResponse({"message": str(e)}, status=400)
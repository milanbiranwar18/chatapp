import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect

from chat.models import Group

# Create your views here.
from user.models import User

logging.basicConfig(filename="chat.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def home_page(request):
    """
    Function for home page
    """
    try:
        if request.method == 'GET':
            group_list = Group.objects.filter(user=request.user).order_by('id')
            return render(request, 'user/home_page.html', {'group_list': group_list})

    except Exception as e:
        logging.error(e)
        return render(request, 'user/home_page.html')


def add_group(request):
    """
    Function for add group
    """
    try:

        if request.method == 'POST':
            data = request.POST
            group = Group.objects.create(name=data.get('name'), user=request.user)
            return redirect("home_page")
        return render(request, 'user/add_group.html')

    except Exception as e:
        logging.error(e)
        return render(request, 'user/home_page.html')


def update_group(request, id):
    """
    Program for update group
    """
    try:
        if request.method == 'POST':
            data = Group.objects.get(id=id)
            data.name = request.POST.get('name')
            data.save()
            return redirect("home_page")
        return render(request, 'user/update.html')
    except Exception as e:
        logging.error(e)
        return render(request, 'user/update.html')


def delete_group(request, id):
    """
    Program for delete group
    """
    try:
        data = Group.objects.get(id=id)
        data.delete()
        return redirect("home_page")
    except Exception as e:
        logging.error(e)



def add_members(request, id):
    try:
        if request.method == 'GET':
            user_list = User.objects.all().exclude(id=request.user.id)
            return render(request, 'user/add_members.html', {"user_list":user_list})
        if request.method == 'POST':
            group = Group.objects.get(id=id)
            group.members.add(*request.POST.get("members"))
            return redirect("home_page")
        return render(request, 'user/add_members.html')
    except Exception as e:
        logging.error(e)
        return render(request, 'user/add_members.html')



# def add_members(request, group_id, user_id):
#     try:
#         if request.method == 'GET':
#             user_list = User.objects.all().exclude(id=request.user.id)
#             return render(request, 'user/add_members.html', {"user_list":user_list})
#         if request.method == 'POST':
#             group = Group.objects.get(id=group_id, user=request.user)
#             user=User.objects.get(id=user_id)
#             group.members.add(user)
#             return redirect("home_page")
#         return render(request, 'user/add_members.html')
#     except Exception as e:
#         logging.error(e)
#         return render(request, 'user/add_members.html')



def view_memnbers(request, id):
    pass

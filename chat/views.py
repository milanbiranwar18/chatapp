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
            group = Group.objects.all().order_by('id')[0:]
            return render(request, 'user/home_page.html', {'group': group})

    except Exception as e:
        print(e)
        logging.error(e)
        return render(request, 'user/home_page.html')


def add_group(request):
    """
    Function for add group
    """
    try:

        if request.method == 'POST':
            obj = request.POST
            group = Group.objects.create(name=obj.get('name'), user=request.user)
            group.save()
            return redirect("home_page")
        return render(request, 'user/add_group.html')

    except Exception as e:
        print(e)
        logging.error(e)


def update_group(request, id):
    """
    Program for update group
    """
    try:
        if request.method == 'POST':
            group = Group.objects.get(id=id)
            group.name = request.POST.get('name')
            group.save()
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
        group = Group.objects.get(id=id)
        group.delete()
        return redirect("home_page")
    except Exception as e:
        logging.error(e)


def view_group(request, id):
    if request.method == 'GET':
        group = Group.members.all().order_by('id')[0:]
        #return render(request, 'user/view_group.html', {'group': group})


def add_members(request, id):

    if request.method == 'GET':
        group = User.objects.all().order_by('id')[0:]

        return render(request, 'user/add_members.html', {'group': group})





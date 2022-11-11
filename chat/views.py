import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from chat.models import Group
from user.models import User

logging.basicConfig(filename="django.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


@login_required
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


@login_required
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
        return render(request, 'user/add_group.html')


@login_required
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


@login_required
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
        return render(request, 'user/home_page.html')


@login_required
def view_group(request, id):
    """
    Function to display members of a group
    """
    try:
        if request.method == 'GET':
            data = Group.objects.get(id=id)
            member_list = data.members.all().values()
            return render(request, 'user/view_group.html', {'member_list': member_list})
    except Exception as e:
        logging.error(e)
        return render(request, 'user/view_group.html')


@login_required
def add_members(request, id):
    """
    Function for adding members in group
    """
    # print(request.POST)
    try:
        if request.method == 'GET':
            user_list = User.objects.all().exclude(id=request.user.id)
            return render(request, 'user/add_members.html', {"user_list": user_list})
        if request.method == 'POST':
            data = Group.objects.get(id=id)
            data.members.add(*request.POST.get('members'))
            return redirect("home_page")
        return render(request, 'user/add_members.html')
    except Exception as e:
        logging.error(e)
        return render(request, 'user/add_members.html')


@login_required
def delete_members(request, id):
    """
    Function for removing members from group
    """
    try:
        data = Group.objects.get(id=id)
        data.members.delete()
        return redirect("view_group")
    except Exception as e:
        logging.error(e)
        return render(request, 'user/view_group.html')

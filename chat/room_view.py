import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from chat.models import Messages


@login_required
def index(request):
    return render(request, "chat/index.html")


@login_required
def room(request, room_name):
    try:
        messages = Messages.objects.filter(group__name=room_name)
        return render(request, "chat/room.html",
                      {"username": request.user.username, "message_list": messages, "room_name": room_name})
    except Exception as e:
        logging.error(e)
        return render(request, "chat/room.html")

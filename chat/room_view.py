from django.shortcuts import render

from chat.models import Messages


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    messages = Messages.objects.filter(group__name=room_name)
    return render(request, "chat/room.html", {"username": request.user.username,  "message_list": messages,  "room_name": room_name})

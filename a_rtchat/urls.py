from django.urls import path
from .views import get_or_create_chatroom

from a_rtchat.views import chat_view, create_groupchat, chatroom_edit_view, chatroom_delete_view, chatroom_leave_view

urlpatterns = [
    path('', chat_view, name="home"),
    path('chat/<username>', get_or_create_chatroom, name="start-chat"),
    path('chat/room/<str:chatroom_name>', chat_view, name="chatroom"),
    path('chat/new_groupchat/', create_groupchat, name="new-groupchat"),
    path('chat/edit/<chatroom_name>', chatroom_edit_view, name="edit-chatroom"),
    path('chat/delete/<chatroom_name>', chatroom_delete_view, name="chatroom-delete"),
    path('chat/leave/<chatroom_name>', chatroom_leave_view, name="chatroom-leave")
 ]
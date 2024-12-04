from django.urls import re_path
from .consumer import *

websocket_urlpatterns = [
    re_path(r'ws/chat/connect_to_liveqa_room/(?P<course_id>\w+)', LiveQAConsumer.as_asgi()),
]
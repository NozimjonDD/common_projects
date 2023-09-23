from django.urls import path

from common.consumers import NumberGenerator

urlpatterns = [
    path('ws/', NumberGenerator.as_asgi(), name='number-generator')
]

# from django.conf.urls import url
#
# from game.consumers import TicTacToeConsumer
#
# websocket_urlpatterns = [
#     url(r'^ws/play/(?P<room_code>\w+)/$', TicTacToeConsumer.as_asgi()),
# ]
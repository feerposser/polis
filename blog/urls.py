from django.urls import path

from .views import index, send_message

urlpatterns = [
    path('', index),
    path('enviar_mensagem/', send_message),
    path('mensagem_enviada/<str:message>', index, name="mensagem_enviada"),
]

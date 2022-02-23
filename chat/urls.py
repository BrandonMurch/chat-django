from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
  path('messages', views.messages, name="messages"),
  path('messages/<int:message_id>', views.message_by_id, name="message"),
  path('users/<int:user_id>', views.user_by_id, name="user"),
  path('send/<int:user_id>', views.message_form, name="message_form")
]

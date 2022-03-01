from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
  path('messages', views.Messages.as_view(), name="messages"),
  path('messages/<int:message_id>', views.message_by_id, name="message"),
  path('users', views.Users.as_view(), name="users"),
  path('users/<int:user_id>', views.user_by_id, name="user"),
  path('send/<int:user_id>', views.message_form, name="message_form")
]

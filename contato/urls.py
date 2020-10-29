from django.urls import path

from . import views

app_name = 'contato'

urlpatterns = [
    path('', views.MessageView.as_view(), name='contato_index')
]
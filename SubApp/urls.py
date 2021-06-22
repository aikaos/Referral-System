from django.urls import path

from . import views

urlpatterns = [
    path('invites/<str:phone_sender>/<str:phone_recipient>/', views.invite)
]
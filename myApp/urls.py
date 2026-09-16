from django.urls import path

from myApp import views

urlpatterns = [
    path("login/", views.login, name='login'),
    path("center/", views.center, name='center'),
    path("centerLeft/", views.centerLeft, name='centerLeft'),
    path("bottomLeft/", views.bottomLeft, name='bottomLeft'),
    path("centerRight/", views.centerRight, name='centerRight'),
    path("centerRightChange/<int:energyType>", views.centerRightChange, name='centerRightChange'),
    path("bottomRight/", views.bottomRight, name='bottomRight')
]

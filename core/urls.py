from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views


# from .views import say_hello

urlpatterns = [
    path("", views.something_cool, name="something_cool"),
    path("/test", views.home, name="home"),
]

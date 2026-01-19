from django.urls import path, include

from .views import home
from . import views   #in 3 and 4 we can use either

urlpatterns = [
    path('', views.home, name='home'),
]
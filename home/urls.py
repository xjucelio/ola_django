from django.urls import path
from . import views

# http://127.0.0.1:8000/
# home/
app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]

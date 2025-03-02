from django.urls import path
from . import views

# http://127.0.0.1:8000/
app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]

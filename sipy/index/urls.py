from django.urls import path,include
from .views import index, blog


app_name = 'index'
urlpatterns = [
    path('', index, name='index'),  # The home page
    path('blog/<slug>', blog, name='blog'),
]

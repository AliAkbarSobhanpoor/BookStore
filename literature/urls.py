from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_book_normal, name='create_book_normal'),
]
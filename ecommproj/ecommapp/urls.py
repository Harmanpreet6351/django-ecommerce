from django.urls import path
from .views import index, about

urlpatterns = [
    path('', view=index),
    path('about', view=about)
]
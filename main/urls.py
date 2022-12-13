from django.urls import path
from .views import (
    salam
)

urlpatterns = [
    path('salam/', salam, name='salam' )
]

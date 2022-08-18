from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('din-var/<int:value>', din_var)
]

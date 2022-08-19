from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsListCreateAPIView.as_view()),
    path('<int:pk>/', NewsUpdateAPIView.as_view()),
    path('details/<int:pk>/', NewsDetailsAPI.as_view())
]

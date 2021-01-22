from django.urls import path

from .views import api_view, APIView


urlpatterns = [
    path('api/', api_view),
    path('api_view/', APIView.as_view()),
]
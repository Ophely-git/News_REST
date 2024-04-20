from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsAPIView.as_view()),
    path('cat/', CategoryAPIView.as_view()),

]
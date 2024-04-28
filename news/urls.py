from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)


from .views import *

router = routers.DefaultRouter()
router.register(r'cat', CategoryViewSet)

urlpatterns = [
    # path('', NewsAPIView.as_view()),
    path('', include(router.urls)),
    path('news/<int:pk>/', NewsAPIView.as_view()),
    path('comm/', CommentsAPIList.as_view()),
    path('comm/<int:pk>/', CommentsAPIDetail.as_view(), name='comment_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
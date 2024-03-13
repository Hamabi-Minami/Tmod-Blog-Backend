from django.urls import path
from apps.UserManager.api import user_api


urlpatterns = [
    path('user/', user_api.UserListCreateAPIView.as_view()),
    path('user/<int:user_id>/', user_api.UserRetrieveUpdateAPIView.as_view())
]


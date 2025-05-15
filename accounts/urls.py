from django.urls import path
from .views import (
    SignUpView,
    UserListView,
    UserUpdateView,
    UserDeleteView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/', SignUpView.as_view(), name='create'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
    
]
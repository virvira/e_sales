from django.urls import path

from core.views import UserCreateView, UserLoginView

urlpatterns = [
    path('signup', UserCreateView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login')
]

from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, CustomLoginView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home_list'), name='logout'),
]
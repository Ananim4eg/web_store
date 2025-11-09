from django.urls import reverse_lazy
from django.views import View

from users.forms import CustomUserCreateForm


class RegisterView(View):
    form_class = CustomUserCreateForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('catalog:home_list')
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from users.forms import CustomUserCreateForm, CustomUserLogin


class RegisterView(FormView):
    form_class = CustomUserCreateForm
    template_name = 'registration.html'
    success_url = reverse_lazy('catalog:home_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        from_email = 'new.mail.test@mail.ru'
        subject = 'Добро пожаловать на наш сайт!'
        message = 'Регистрация прошла успешно. Спасибо, что выбрали нас!'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    form_class = CustomUserLogin
    template_name = 'login.html'




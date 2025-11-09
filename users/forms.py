from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "username", "password1", "password2")

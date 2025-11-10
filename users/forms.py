from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    def __init__(self, *args, **kwargs):
        super(CustomUserCreateForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "password1", "password2")

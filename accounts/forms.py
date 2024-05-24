from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser # 連携するUserモデルを設定
        fields = ('username', 'password1','password2') # フォームで使用するフィールドを設定する
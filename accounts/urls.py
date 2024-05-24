from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('サインアップ/', views.SignUpView.as_view(), name='signup'),
    path('登録完了/', views.SignUpSuccessView.as_view(), name='signup_success'),
]
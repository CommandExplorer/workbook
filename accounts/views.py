from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm # 使用するフォームクラスを指定
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success') # フォームの処理が成功した後にリダイレクトするURLを指定
    
    def form_valid(self, form): # フォームの検証が成功したときに呼び出される
        user = form.save() # フォームに入力されたデータを保存し、新しいユーザーオブジェクトを作成する
        self.objects = user # 新しく作成されたユーザーオブジェクトをインスタンス変数に格納する
        return super().form_valid(form) # リダイレクト処理を行う
    
class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"
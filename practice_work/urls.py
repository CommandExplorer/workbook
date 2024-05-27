from django.urls import path
from .views import PracticeWorkView

app_name = 'practice_work'

urlpatterns = [
    path('work/', PracticeWorkView.as_view(), name='work'),
]
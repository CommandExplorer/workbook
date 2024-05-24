from django.urls import path
from .views import ChapterListView

app_name = 'workbook'

urlpatterns = [
    path('章選択/', ChapterListView.as_view(), name='chapter_select'),
]
from django.urls import path
from .views import IndexView, ChapterListView, QuestionListView, QuestionDetailView, AnswerDetailView

app_name = 'workbook'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('章選択/', ChapterListView.as_view(), name='chapter_select'),
    path('<str:chapter>/', QuestionListView.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('answer/<int:pk>/', AnswerDetailView.as_view(), name='answer_detail'),
]
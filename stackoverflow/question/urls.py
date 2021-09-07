from django.urls import path
from .views import QuestionCreateView, QuestionUpdateView, QuestionDeleteView, QuestionDetailView, QuestionListView

app_name = "question"

urlpatterns = [
    path('', QuestionListView.as_view(), name='questions'),
    path('new/', QuestionCreateView.as_view(), name='question-create'),
    path('<slug:slug>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('<slug:slug>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('<slug:slug>/', QuestionDetailView.as_view(), name='question-detail'),
]

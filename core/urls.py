from django.urls import path

from core.views import ChecklistsAPIView,CheckListAPIView,CheckListItemCreateAPIView
from django.urls import path

urlpatterns = [
    path('api/checklists/',ChecklistsAPIView.as_view()),
    path('api/checklist/<int:pk>/',CheckListAPIView.as_view()),
    path('api/checklistItem/Create/',CheckListItemCreateAPIView.as_view()),
]

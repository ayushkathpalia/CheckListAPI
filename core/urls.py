from django.urls import path

from core.views import TestAPIView,ChecklistAPIView
from django.urls import path

urlpatterns = [
    path('', TestAPIView.as_view()),
    path('api/checklists/',ChecklistAPIView.as_view()),
]

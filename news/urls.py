# urls.py
from django.urls import path
from .views import (
    NewsCreateView,
    NewsListView,
    NewsDetailView,
    NewsUpdateView,
    NewsDeleteView
)

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/create/', NewsCreateView.as_view(), name='news-create'),
    path('news/<int:id>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:id>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:id>/delete/', NewsDeleteView.as_view(), name='news-delete'),
]

from django.urls import path
from .views import HomePageView, PostDetailView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('blog/<int:pk>', PostDetailView.as_view(), name='blog'),
]
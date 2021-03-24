from django.urls import path
from django.views.generic import TemplateView
from .views import UserExperienceView

urlpatterns = [
    path('post-exp/<str:pk>/',UserExperienceView.as_view(), name="create-exp")
]
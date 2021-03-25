from django.urls import path
from django.views.generic import TemplateView
from .views import UserExperienceView, UserExperienceDetail, UserProjectView, UserProjectDetails

urlpatterns = [
    path('get-exp/<str:id>/', UserExperienceDetail.as_view(), name="get-up-del-exp"),
    path('list-exp/', UserExperienceView.as_view(), name="create/list-exp"),
    path('get-project/<str:id>/',UserProjectDetails.as_view(), name="get-up-del-project"),
    path('list-project/', UserProjectView.as_view(), name="create/list-project"),

]
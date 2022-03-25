from django.urls import path
from presentation import views

urlpatterns = [
    path("", views.presentation, name="presentation"),
    path("infos", views.infos, name="infos"),
    path("agreement", views.agreement, name="agreement"),
    path("policy", views.policy, name="policy"),
]

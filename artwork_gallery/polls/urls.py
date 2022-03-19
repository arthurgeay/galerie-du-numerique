from django.urls import path
from polls import views

urlpatterns = [
    path("<int:id>", views.add_vote, name="add_vote"),
]

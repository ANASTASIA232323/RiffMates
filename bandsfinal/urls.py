from django.urls import path
from bandsfinal import views

urlpatterns = [
    path("musician/<int:musician_id>", views.musician, name="musician")
]

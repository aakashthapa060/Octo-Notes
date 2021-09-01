from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.index, name = "index"),
    path("delete/note/<int:id>/", views.delete_note, name = "deleteNote")
]
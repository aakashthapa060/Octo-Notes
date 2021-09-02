from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.index, name = "index"),
    path("personal/", views.personalNote, name = "personalNote"),

    path("delete/note/<int:id>/", views.delete_note, name = "deleteNote")
]
from django import forms
from django.forms import fields
from django.forms.widgets import TextInput
from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(widget = TextInput( attrs= {
        "id": "noteTitle",
        "class": "noteTitle",
        "placeholder": "Title"
    }))
    content = forms.CharField(widget = TextInput( attrs= {
        "id": "noteContent",
        "class": "noteContent",
        "placeholder": "Content"
    }))
    class Meta:
        model = Note
        fields = ("title","content","privacy")
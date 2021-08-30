from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.

def index(request):
    note = Note.objects.all()
    context = {
        "notes": note
    }
    return render(request, "index.html",context)

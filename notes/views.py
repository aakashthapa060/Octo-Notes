from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note

# Create your views here.

def index(request):
    note = Note.objects.all()
    context = {
        "notes": note
    }
    return render(request, "index.html",context)

def delete_note(request, id):
    note = Note.objects.get(pk = id)
    note.delete()

    return redirect("notes:index")
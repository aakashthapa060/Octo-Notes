from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        note = Note.objects.all()
        noteForm = NoteForm(request.POST or None)
        if noteForm.is_valid():
            activeUser = request.user
            title = noteForm.cleaned_data["title"]
            content = noteForm.cleaned_data["content"]
            privacy = noteForm.cleaned_data["privacy"]
            noteCreated = Note.objects.create(user = activeUser, title = title, content = content, privacy= privacy)
            noteCreated.save()
            return redirect("notes:index")
        else:
            noteForm = NoteForm()

        context = {
            "notes": note,
            "form": noteForm,
        }
        return render(request, "index.html",context)
    else:
        return redirect("users:login")

def delete_note(request, id):
    note = Note.objects.get(pk = id)
    if note.privacy == "private":
        note.delete()
        return redirect("notes:personalNote")
    else:
        note.delete()
        return redirect("notes:index")

def personalNote(request):
    if request.user.is_authenticated:
        user = request.user
        privatePost = user.note_set.filter(privacy = "private")
        context = {
            "privatePost": privatePost
        }
        return render(request, "note/private.html", context)
    else:
        return redirect("users:login")
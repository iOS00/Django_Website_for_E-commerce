from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Meeting, Room
from .forms import MeetingForm

def detail (request, id):
    meeting= get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms_list (request):
    return render (request,
                   "meetings/rooms_list.html",
                   {"rooms": Room.objects.all()})

def new (request):
    if request.method =="POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Successfully saved {form.cleaned_data['title']}"
            )
            return redirect("welcome")
        else:
            messages.error(
                request,
                'Failed to create a new meeting... Please try again.'
            )
    else:
        form = MeetingForm()
    return render (request, "meetings/new.html", {"form": form})



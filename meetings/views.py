from django.forms import modelform_factory
from django.shortcuts import redirect, render, get_object_or_404
from .models import Meeting, Room
from django.forms import modelform_factory
# Create your views here.


def meeting_detail(request, id):
    meet = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/meeting.html", {"meeting_detail": meet})


def room_list(request):
    all_rooms = Room.objects.all()
    return render(request, "meetings/all_rooms.html", {"rooms": all_rooms})


MeetingForm = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request,"meetings/new_meeting.html",{"form":form})

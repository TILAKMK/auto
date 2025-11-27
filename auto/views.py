#from
from django.shortcuts import render, redirect
from .forms import BookingForm
def home(request):
    return render(request, "auto/home.html")

def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = BookingForm()

    return render(request, "auto/booking_form.html", {"form": form})

def success(request):
    return render(request, "auto/success.html")

from django import forms
from .models import Booking
import datetime

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set today's date as minimum
        self.fields['date'].widget.attrs['min'] = datetime.date.today().isoformat()

    # ---- Services Dropdown ----
    SERVICE_CHOICES = [
        ("Foam Washing", "Foam Washing"),
        ("Interior Dry Cleaning", "Interior Dry Cleaning"),
        ("Rubbing & Polishing", "Rubbing & Polishing"),
        ("Ceramic Coating", "Ceramic Coating"),
        ("Sanitization", "Sanitization"),
        ("Engine Bay Detailing", "Engine Bay Detailing"),
    ]

    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        label="Select Service"
    )

    # ---- Time Dropdown ----
    TIME_CHOICES = [
        (f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
        for hour in range(9, 16)
        for minute in (0, 30)
    ]

    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        label="Choose Time"
    )

    # ---- Date Field ----
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'text',  # required for Flatpickr popup
                'placeholder': 'Select a date'
            }
        ),
        label="Choose Date"
    )

    class Meta:
        model = Booking
        fields = "__all__"

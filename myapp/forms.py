from django import forms
from .models import Profile,Visitor

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = [
            'profile_picture','name','emp_id','email',
            'designation','department','reporting_to','mobile'
        ]

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'visitor_name','visitor_email','category',
            'appointment_date','appointment_time','reason',
            'designated_attendee','document'
        ]

class RescheduleMeetForm(forms.ModelForm):
    class Meta:
        model=Visitor
        fields = [
            'appointment_date','appointment_time' 
            # Allow only date and time to be updated
        ]

        widgets = {
            'appointment_date': forms.DateInput(attrs={'type':'date', 'class': 'form_control'}),
            'appointment_time': forms.TimeInput(attrs={'type':'time', 'class': 'form_control'}),
        }

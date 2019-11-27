from django import forms

from .models import Visitor

class CheckinForm(forms.ModelForm):
    visitorName = forms.CharField(widget=forms.TextInput(attrs={
        "id": "visitorName",
        "class": "form-control",
        "placeholder": "Name",
        "autofocus": "True"
    }))
    visitorEmail = forms.EmailField(widget=forms.EmailInput(attrs={
        "id": "visitorEmail",
        "class": "form-control",
        "placeholder": "Email Address"
    }))
    visitorContactNo = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={"invalid": "Enter a valid number"}, widget=forms.TextInput(attrs={
        "id": "visitorContactNo",
        "class": "form-control",
        "placeholder": "Phone No"
    }))
    hostName = forms.CharField(widget=forms.TextInput(attrs={
        "id": "hostName",
        "class": "form-control",
        "placeholder": "Name"
    }))
    hostEmail = forms.EmailField(widget=forms.EmailInput(attrs={
        "id": "hostEmail",
        "class": "form-control",
        "placeholder": "Email Address"
    }))
    hostContactNo = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={"invalid": "Enter a valid number"}, widget=forms.TextInput(attrs={
        "id": "hostContactNo",
        "class": "form-control",
        "placeholder": "Phone No"
    }))
    class Meta:
        model = Visitor
        fields = [
            'visitorName',
            'visitorEmail',
            'visitorContactNo',
            'hostName',
            'hostEmail',
            'hostContactNo'
        ]
    
    def clean_visitorEmail(self):
        email = self.cleaned_data["visitorEmail"]
        try:
            visitor = Visitor.objects.get(visitorEmail=email, checkOut__isnull=True)
            print(visitor)
        except Visitor.DoesNotExist:
            visitor = None
        if visitor is None: 
            return email
        else:
            raise forms.ValidationError("Email already exists")
 
    

class CheckoutForm(forms.ModelForm):
    visitorEmail = forms.EmailField(widget=forms.EmailInput(attrs={
        "id": "visitorEmail",
        "class": "form-control",
        "placeholder": "Email Address",
        "autofocus": "True"
    }))
    class Meta:
        model = Visitor
        fields = [
            'visitorEmail'
        ]

    def clean_visitorEmail(self):
        email = self.cleaned_data["visitorEmail"]
        try:
            visitors = Visitor.objects.filter(visitorEmail=email)
        except Visitor.DoesNotExist:
            visitors = None

        if visitors: 
            for visitor in visitors:
                if not visitor.checkOut:
                    return email
            raise forms.ValidationError("User already checked-out")
        else:
            raise forms.ValidationError("Email address not found")
    


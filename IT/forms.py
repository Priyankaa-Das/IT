from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'company', 'message', 'agree_terms']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'class': 'form-control',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email address',
                'class': 'form-control',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control'
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Company/Services',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Information Message',
                'class': 'form-control',
                'rows': 5,
                'required': True
            }),
            'agree_terms': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField(required=True)
    user_email = forms.EmailField(required=True)
    user_subject = forms.CharField(required=True)
    user_message = forms.CharField(widget=forms.Textarea, required=True)
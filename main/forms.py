from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Your name",
        required=True, 
        max_length = 50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name',
            'type': 'text',
            'class' : 'form-control'})
    )
    email_address = forms.EmailField(
        label="Email address",
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your email address',
            'type': 'email',
            'class' : 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message',
            'type': 'text',
            'class' : 'form-control'}),
        required=True, 
        max_length = 2000
    )
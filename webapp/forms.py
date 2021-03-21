from django import forms 

class ContactForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100, required=True)
    last_name = forms.CharField(label='last_name', max_length=100, required=True)    
    email = forms.EmailField(label='email', required=True)
    phone = forms.CharField(label='phone', required=False)
    subject = forms.CharField(label='subject', max_length=100, required=True)
    message = forms.CharField(label='message', required=True, max_length=500)
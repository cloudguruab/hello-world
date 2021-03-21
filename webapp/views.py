from django.shortcuts import render
from django.http import request, HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactModel

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            
            context = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone, 'subject': subject, 'message': message}
            details = f'{first_name} {last_name}: {email}, {message}'
            send_mail(request.POST['subject'], details, settings.EMAIL_HOST_USER, ['ap.brown011@gmail.com'])
            
            ContactModel.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            
            return render(request, 'submit.html', context=context)
        else:
            return render(request, 'error.html')
        
    return render(request, 'contact.html')


# def submit(request):
#     return render(request, 'submit.html')
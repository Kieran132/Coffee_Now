from django.shortcuts import render
from django.views import generic
from .models import ContactForm
from django.views.generic import View
from django.core.mail import send_mail
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print("This is message:", message)
        print("This is email:", email)

        send_mail(
            'Contact Form Submission from {}'.format(name),
            message,
            email,
            ['banginburgers23@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'contact.html')

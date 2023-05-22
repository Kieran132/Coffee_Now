from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import ContactForm
from django.views.generic import View
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages


def contact(request):
    """
    Function obtains the users input fields then uses Google smtp backend
    server to send the information to an external email
    """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print("This is name:", name)
        print("This is message:", message)
        print("This is email:", email)

        send_mail(
            'Contact Form Submission from {}'.format(name + ', ' + email),
            message,
            email,
            ['coffeenowCI23@gmail.com'],
            fail_silently=False,
        )
        print(" After send mail....")

    return render(request, 'contact.html')

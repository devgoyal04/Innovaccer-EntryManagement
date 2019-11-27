from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.utils import timezone
import requests

from .models import Visitor
from .forms import CheckinForm, CheckoutForm

url = "https://www.fast2sms.com/dev/bulk"


def HomeView(request):
    return render(request, 'home.html', {})

def CheckinView(request):
    form = CheckinForm(request.POST or None)
    if form.is_valid():
        form.save()
        visitor = Visitor.objects.get(visitorEmail = form.cleaned_data.get('visitorEmail'), checkOut__isnull=True)
        check_in = visitor.checkIn.strftime('%B %d, %Y %l:%M:%S %p')
        my_msg = f'{visitor.visitorName} is here to meet you\nCheck-in Time: {check_in}\nContact Number: {visitor.visitorContactNo}\nEmail Address: {visitor.visitorEmail}'
        try:
            send_mail(
                    f'{visitor.visitorName} just checked in',
                    my_msg,
                    settings.EMAIL_HOST_USER,
                    [visitor.hostEmail],
                    fail_silently=True
                )
        except BadHeaderError:
            return redirect('details:home')

        host_num = visitor.hostContactNo
        auth_token = settings.AUTH_TOKEN

        payload = f"sender_id=FSTSMS&message={my_msg}&language=english&route=p&numbers={host_num}"
        headers = {
            'authorization': auth_token,
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        messages.success(request, f"{visitor.visitorName} successfully checked in")
        return redirect('details:home')

    my_context = {
        'form': form
    }
    return render(request, 'checkin.html', my_context)

def CheckoutView(request):
    form = CheckoutForm(request.POST or None)
    if form.is_valid():
        visitor = Visitor.objects.get(visitorEmail=form.cleaned_data.get('visitorEmail'), checkOut__isnull=True)
        visitor.checkOut = timezone.now()
        visitor.save()
        check_out = visitor.checkOut.strftime('%B %d, %Y %l:%M:%S %p')
        check_in = visitor.checkIn.strftime('%B %d, %Y %l:%M:%S %p')
        my_msg = f"Name: {visitor.visitorName}\nPhone No.: {visitor.visitorContactNo}\nCheck-in Time: {check_in}\nCheck-out Time: {check_out}\nHost Name: {visitor.hostName}\nAddress visited: Innovacer Office"
        try:
            send_mail(
                    f'Your Visit to Innovacer',
                    my_msg,
                    settings.EMAIL_HOST_USER,
                    [visitor.visitorEmail],
                    fail_silently=True
                )
        except BadHeaderError:
            return redirect('details:home')
        
        messages.success(request, f"{visitor.visitorName} successfully checked out")
        return redirect('details:home')

    my_context = {
        'form': form
    }
    return render(request, 'checkout.html', my_context)
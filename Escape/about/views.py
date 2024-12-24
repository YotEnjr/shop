from django.shortcuts import render


def about(request):
    return render(request, 'about/about.html', {})


def contact(request):
    return render(request, 'about/contact.html', {})


def deliver(request):
    return render(request, 'about/delivery.html', {})


def payment(request):
    return render(request, 'about/payment.html', {})

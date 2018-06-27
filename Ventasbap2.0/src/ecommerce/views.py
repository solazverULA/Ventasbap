from django.contrib.auth import authenticate, login, get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from .forms import ContactForm

def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    context = {
        "title":"Hello World!",
        "content":" Welcome to the homepage.",

    }
    if request.user.is_authenticated():
        context["premium_content"] = "YEAHHHHHH"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About Page",
        "content":" Welcome to the about page."
    }
    return render(request, "about/about.html", context)

def contact_page(request):
    if request.method == 'GET':

        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ventasbap@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, "contact/view.html")

def faq_page(request):
    context = {
        "title":"FAQ Page",
        "content":" Welcome to the FAQ page."
    }
    return render(request, "faq/faq.html", context)










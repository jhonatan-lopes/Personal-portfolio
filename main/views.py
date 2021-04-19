from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Education, Expertise, Experience
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from publications.models import MyInfo

def home(request):
    home_context = {}
    home_context["my_info"] = MyInfo.load()
    return render(request,"main/home.html", context=home_context)

def about(request):
    about_context = {}

    about_context["educations"] = Education.objects.all().order_by("-end_date")
    about_context["expertises"] = Expertise.objects.all()
    about_context["experiences"] = Experience.objects.all().order_by("end_date")

    return render(request, "main/about.html", context=about_context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.META['HTTP_HOST'] + " Inquiry - " + form.cleaned_data['name']
            body = {
                'name': form.cleaned_data['name'], 
                'email': form.cleaned_data['email_address'], 
                'message':form.cleaned_data['message'], 
            }
            sender = form.cleaned_data['email_address']
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, sender, [MyInfo.load().email]) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your message was sent successfuly!')
            return redirect ("contact")
      
    form = ContactForm()
    return render(request, "main/contact.html", {'form':form})
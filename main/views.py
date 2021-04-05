from django.shortcuts import render
from .models import Education, Expertise, Experience

# Create your views here.
def home(request):
    return render(request,"main/home.html")

def about(request):
    about_context = {}

    about_context["educations"] = Education.objects.all().order_by("-end_date")
    about_context["expertises"] = Expertise.objects.all()
    about_context["experiences"] = Experience.objects.all().order_by("end_date")

    return render(request, "main/about.html", context=about_context)


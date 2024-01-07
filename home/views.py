from django.shortcuts import render
from django.views import View
from .models import ContactUs, Skill,Person
from django.contrib.auth.models import User


# Create your views here.

class hello(View):
    def get(self, request):
        user = User.objects.get(email='abasghlipour@gmail.com')
        contact = ContactUs.objects.get(email=user.email)
        skills = Skill.objects.all()
        person=Person.objects.get(user=user)
        return render(request, 'base.html', {'user': user, 'contact': contact, 'skills': skills,'person':person})

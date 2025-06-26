from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'お問い合わせ: ' + cd['name']
            message = f"名前: {cd['name']}\nメール: {cd['email']}\n\n{cd['message']}"
            send_mail(subject, message, 'noreply@example.com', ['a.m.techcat@gmail.com'])
            
            messages.success(request, 'お問い合わせを送信しました。ありがとうございました。')
            form = ContactForm()
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')
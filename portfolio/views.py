from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.views.generic import DetailView
from .models import Project


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

def inventory_detail_view(request):
    return render(request, 'inventory_detail.html')  # ← 作成するテンプレート

def project_detail(request, slug): 
    project = get_object_or_404(Project, slug=slug)

    # slugに応じてテンプレートを切り替える
    if slug == 'quake-viz':
        template_name = 'quake_detail.html'
    elif slug == 'inventory-manager':
        template_name = 'inventory_detail.html'
    elif slug == 'co2-viz':
        template_name = 'co2_detail.html'
    else:
        template_name = 'project_detail.html'

    return render(request, template_name, {'project': project})

def quake_detail_view(request):
    return render(request, 'quake_detail.html')

def co2_detail_view(request):
    return render(request, 'co2_detail.html')

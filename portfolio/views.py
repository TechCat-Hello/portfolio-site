from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail  # 開発時は print でもOK
from .forms import ContactForm


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send_mail(...) ここは開発中なら print で代用
            print(form.cleaned_data)
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
